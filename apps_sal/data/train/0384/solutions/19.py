class Solution:
    # def sumSubseqWidths(self, A: List[int]) -> int:
    #     A = sorted(A)
    #     total, cur, cnt = 0, 0, 0
    #     MOD = 10**9 + 7
    #     for i in range(1,len(A)):
    #         cnt *= 2
    #         cnt += 1
    #         cur *= 2
    #         cur += (A[i]-A[i-1])*cnt
    #         cur %= MOD
    #         total += cur
    #         total %= MOD
    #         # print(cur,cnt)
    #     return total

    def sumSubseqWidths(self, A):
        return sum(((1 << i) - (1 << len(A) - i - 1)) * a for i, a in enumerate(sorted(A))) % (10**9 + 7)
