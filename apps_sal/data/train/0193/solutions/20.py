class Solution:

    def minSetSize(self, arr: List[int]) -> int:
        n = len(arr) // 2
        freq = {}
        for i in arr:
            if i in freq:
                freq[i] += 1
            else:
                freq[i] = 1
        res = [i for i in freq.values()]
        res.sort(reverse=True)
        total = 0
        count = 0
        for i in res:
            total += i
            count += 1
            if total >= n:
                return count
