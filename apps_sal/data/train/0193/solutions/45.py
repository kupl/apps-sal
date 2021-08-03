class Solution:
    def minSetSize(self, arr: List[int]) -> int:
        c = Counter(arr)
        c = list(c.values())
        c.sort(reverse=True)
        k = len(c) // 2
        s = 0
        count = 0
        for i in range(len(c)):
            s += c[i]
            count += 1
            if s >= len(arr) // 2:
                return count
