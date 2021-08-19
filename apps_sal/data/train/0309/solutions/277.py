class Solution:
    def longestArithSeqLength(self, A: List[int]) -> int:

        if len(A) == 1:
            return 1
        if len(A) == 2:
            return 2
        N = len(A)
        ans = 2
        seen = {}
        for i in range(N):
            for j in range(i + 1, N):
                diff = A[j] - A[i]
                # now for the rest can we do this diff?

                if (i, diff) in seen:
                    ans = max(ans, seen[i, diff] + 1)
                    seen[j, diff] = seen[i, diff] + 1
                else:
                    seen[j, diff] = 2

                # # prev=A[j]
                # # for k in range(j+1,N):
                # #     if A[k]-prev==diff:
                # #         curr+=1
                # #         prev=A[k]
                # ans=max(ans,curr)

            # seen.add(A[i])
        return ans


#         if N<=2:
#             return N

#         dp=[0]*N

#         dp[2]=3 if A[2]-A[1]==A[1]-A[0] else 0

#         ans=dp[2]

#         for i in range(3,N):
#             if A[i]-A[i-1]==A[i-1]-A[i-2]:
#                 ans=max(ans,dp[i-1]+1,3)
#                 dp[i]=max(1+dp[i-1],3)

#         return ans

#         N=len(A)
#         def rec(diff,i,m):
#             if (i,diff) in m:
#                 return m[i,diff]

#             if i==N:
#                 return 0

#             m[i,diff]=0

#             ans=0

#             for k in range(i+1,N):
#                 if A[k]-A[i]==diff:
#                     ans=1+rec(diff,k+1,m)
#                     break

#             # make a new diff
#             # ans=max(ans,rec(diff,i+1,m))

#             for k in range(i+1,N):
#                 ans=max(ans,2+rec(A[k]-A[i],k+1,m))

#             m[i,diff]=ans
#             return ans

#         return rec(float('inf'),0,{})

#             if A[i]-diff in seen and seen[A[i]-diff]==i-:
#                 seen[A[i]]=i
#                 print('found',A[i],diff,i,seen)
#                 m[i,diff]=1+rec(diff,i+1,seen,m)
#             else:
#                 m[i,diff]=rec(diff,i+1,seen,m)

#             return m[i,diff]


#         N=len(A)
#         ans=0
#         m={}
#         for i in range(N):
#             for j in range(i+1,N):
#                 diff=A[j]-A[i]
#                 if diff!=0:
#                     seen={A[j]:1, A[i]:0}
#                     ans=max(ans,2+rec(diff,j+1,seen,m))

#         return ans
