from collections import Counter


class Solution:

    def minSetSize(self, arr: List[int]) -> int:
        c = Counter(arr)
        (a, res) = (0, 0)
        for (n, c) in c.most_common():
            a += c
            res += 1
            if a >= len(arr) // 2:
                break
        return res
