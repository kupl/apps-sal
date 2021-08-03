class Solution:
    def longestOnes(self, arr: List[int], k: int) -> int:
        hashmap = dict()
        max_len = length = start_index = 0
        hashmap[0] = 0
        hashmap[1] = 0
        for i in arr:
            hashmap[i] += 1
            if hashmap[0] > k:
                hashmap[arr[start_index]] -= 1
                start_index += 1
            max_len = max(max_len, sum(hashmap.values()))

        return max_len
