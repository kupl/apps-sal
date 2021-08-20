class Solution:

    def longestSubsequence(self, arr: List[int], difference: int) -> int:
        record = {}
        for i in range(len(arr)):
            a = arr[i]
            if a - difference in record:
                record[a] = record[a - difference] + 1
            else:
                record[a] = 1
        return max(list(record.values()))
