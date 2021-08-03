from collections import defaultdict


class Solution:
    def countTriplets(self, arr: List[int]) -> int:
        n = len(arr)
        x = [0]
        for t in arr:
            x.append(x[-1] ^ t)
        ans = 0
        for i in range(n):
            for j in range(i + 1, n):
                for k in range(j, n):
                    if x[j] ^ x[i] == x[k + 1] ^ x[j]:
                        ans += 1

        return ans
