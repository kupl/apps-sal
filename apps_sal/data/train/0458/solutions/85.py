class Solution:
    def minSubarray(self, nums: List[int], p: int) -> int:
        prefix_sum_map = {0: [-1]}
        cur_sum = 0

        for index, num in enumerate(nums):
            cur_sum = (cur_sum + num) % p
            if not cur_sum in prefix_sum_map:
                prefix_sum_map[cur_sum] = []
            prefix_sum_map[cur_sum].append(index)

        if cur_sum == 0:
            return 0

        result = len(nums)

        for prefix_sum, index_ary in list(prefix_sum_map.items()):
            target_sum = (prefix_sum - cur_sum) % p
            if target_sum in prefix_sum_map:
                target_ary = prefix_sum_map[target_sum]
                for i in range(len(index_ary)):
                    for j in range(len(target_ary)):
                        if target_ary[j] > index_ary[i]:
                            continue
                        result = min(result, index_ary[i] - target_ary[j])

        if result == len(nums):
            result = -1
        return result
