from collections import Counter


class Solution:

    def threeSumMulti(self, A: List[int], target: int) -> int:
        countA = Counter(A)
        ans = 0
        done = set()
        M = int(1000000000.0 + 7)
        for (i, j) in list(countA.items()):
            for (k, l) in list(countA.items()):
                req = target - i - k
                temp = tuple(sorted([i, k, req]))
                if temp not in done:
                    done.add(temp)
                    if i == k == req:
                        ans += j * (j - 1) * (j - 2) // 6
                    if i == k and i != req:
                        ans += j * (j - 1) // 2 * countA[req]
                    if i != k and i == req:
                        ans += l * (j * (j - 1)) // 2
                    if i != k and k == req:
                        ans += j * (l * (l - 1)) // 2
                    if i != k and k != req:
                        ans += j * l * countA[req]
                    ans %= M
        return ans
