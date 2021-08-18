class Solution:
    def findLatestStep(self, arr: List[int], m: int) -> int:
        from collections import Counter
        n = len(arr)
        mem = [0] * n
        counter = Counter()
        res = -1
        for j, v in enumerate(arr):
            i = v - 1
            mem[i] = 1
            l = mem[i - 1] if i - 1 >= 0 else 0
            r = mem[i + 1] if i + 1 < n else 0
            counter[l] -= 1
            counter[r] -= 1
            cur = l + r + 1
            mem[i - l], mem[i + r] = cur, cur
            counter[cur] += 1
            if counter[m] > 0:
                res = j + 1
        return res
