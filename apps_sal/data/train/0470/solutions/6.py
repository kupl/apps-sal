from collections import Counter
class Solution:
    def threeSumMulti(self, A: List[int], target: int) -> int:
        MOD = 10 ** 9 + 7
        if len(A) < 3:
            return 0
        counts = Counter(A)
        keys = sorted(counts.keys())
        n, res = len(keys), 0
        
        for i, a in enumerate(keys):
            T = target - a
            j, k = i, n - 1
            while j <= k:
                b, c = keys[j], keys[k]
                if b + c < T:
                    j += 1
                elif b + c > T:
                    k -= 1
                else:
                    if i < j < k:
                        res += counts[a] * counts[b] * counts[c] 
                    elif i == j < k:
                        res += counts[a] * (counts[a] - 1) // 2 * counts[c]
                    elif i < j == k:
                        res += counts[a] * counts[b] * (counts[b] - 1) // 2
                    else:
                        res += counts[a] * (counts[a] - 1) * (counts[a] - 2) // 6
                    j += 1
                    k -= 1
        return res % MOD
