class Solution:
    #     def findUnique(self, l):
    #         u = []

    #         for num in l:
    #             if num not in u:
    #                 u.append(num)

    #         return self.findOR(u)

    #     def findOR(self, l):

    #         ret = 0

    #         for num in l:
    #             ret = self.doBin(ret, num)
    #         return ret

    #     def doBin(self, a, b):

    #         p = 0

    #         ret = 0
    #         while a or b:
    #             if a%2 or b%2:
    #                ret += pow(2,p)
    #             p +=1
    #             a, b = a//2, b//2

    #         return ret

    #     def subarrayBitwiseORs(self, A: List[int]) -> int:
    #         #just unique combinations

    #         res = 0

    #         seen = []
    #         #brute force
    #         for i in range(len(A)):
    #             for j in range(i,len(A)):
    #                 uniq = self.findUnique(A[i:j+1])
    #                 if uniq not in seen:
    #                     seen.append(uniq)
    #                     res +=1

    #         return res

    def subarrayBitwiseORs(self, A):
        ans = set()
        cur = {0}
        for x in A:
            cur = {x | y for y in cur} | {x}
            ans |= cur
        return len(ans)
