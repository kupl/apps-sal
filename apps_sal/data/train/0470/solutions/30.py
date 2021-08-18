class Solution:
    def threeSumMulti(self, A: List[int], target: int) -> int:
        counter = [0] * 101
        for num in A:
            counter[num] += 1
        count = 0
        MOD = int(10 ** 9 + 7)
        for i in range(len(A) - 2):
            counter[A[i]] -= 1
            residual = target - A[i]
            for Aj in range(101):
                Ak = residual - Aj
                if Ak >= 0 and Ak <= 100 and Aj <= Ak:
                    if Aj != Ak:
                        count += counter[Aj] * counter[Ak]
                    else:
                        count += (counter[Aj] * (counter[Aj] - 1)) // 2
        return count % MOD
