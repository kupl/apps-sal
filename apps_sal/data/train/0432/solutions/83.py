class Solution:
    def isPossibleDivide(self, nums: List[int], k: int) -> bool:
        if len(nums) % k != 0:
            return False

        m = int(len(nums) / k)

        res = []

        count = {}

        for i in range(len(nums)):
            if not count.get(nums[i]):
                count[nums[i]] = 0
            count[nums[i]] += 1

        arr = []
        for i in range(m):
            ks = list(count.keys()).copy()
            ks.sort()
            for j in range(len(ks)):
                if len(arr) == 0 or arr[len(arr) - 1] == ks[j] - 1:
                    arr.append(ks[j])
                    count[ks[j]] -= 1
                    if count[ks[j]] == 0:
                        del count[ks[j]]
                else:
                    return False

                if len(arr) == k:
                    res.append(arr.copy())
                    arr.clear()
                    break
        if len(count) > 0:
            return False

        return True
