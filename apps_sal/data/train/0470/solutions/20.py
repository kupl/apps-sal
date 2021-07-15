# from collections import Counter

# class Solution(object):
#     def threeSumMulti(self, A, target):
#         MOD = 10**9 + 7
#         count = [0] * 101
#         for x in A:
#             count[x] += 1

#         ans = 0

#         # All different
#         for x in range(101):
#             for y in range(x+1, 101):
#                 z = target - x - y
#                 if y < z <= 100:
#                     ans += count[x] * count[y] * count[z]
#                     ans %= MOD

#         # x == y
#         for x in range(101):
#             z = target - 2*x
#             if x < z <= 100:
#                 ans += count[x] * (count[x] - 1) / 2 * count[z]
#                 ans %= MOD

#         # y == z
#         for x in range(101):
#             if (target - x) % 2 == 0:
#                 y = (target - x) / 2
#                 if x < y <= 100:
#                     ans += count[x] * count[y] * (count[y] - 1) / 2
#                     ans %= MOD

#         # x == y == z
#         if target % 3 == 0:
#             x = target / 3
#             if 0 <= x <= 100:
#                 ans += count[x] * (count[x] - 1) * (count[x] - 2) / 6
#                 ans %= MOD

#         return ans

from collections import Counter,defaultdict

class Solution:
    def threeSumMulti(self, A: List[int], target: int) -> int:
        
        A.sort()
        dic= defaultdict(list)
        count = Counter(A)
        B=list(count.keys())*3
        B.sort()
        
        seen=set()
        
        ans=0
        
        for i in range(len(B)):
            dic[B[i]].append(i)
        
        for i in range(len(B)-2):
            for j in range(i+1, len(B)-1):
                temp=target-B[i]-B[j]
                
                if temp in dic:
                    k=dic[temp][-1]

                    if k>j:
                        seen.add((B[i],B[j],B[k]))  
        
        def comb(n,m):
            N=list(range(n-m+1,n+1))
            M=list(range(1,m+1))
            
            nn=1
            mm=1
            for i in N:
                nn*=i
            
            for i in M:
                mm*=i
                
            return int(nn/mm)
        
        for t in seen:
            temp=1
            c=Counter(t)
            print(t)
            for i in c:
                m=c[i]
                n=count[i]
                if m>n:
                    temp=0
                    break
                temp*=comb(n,m)
            ans+=temp
                
            
        return ans%(10**9+7)

