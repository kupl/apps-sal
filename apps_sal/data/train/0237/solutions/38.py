class Solution:
    def numSubarraysWithSum(self, A: List[int], S: int) -> int:
        P = [0]
        for x in A: P.append(P[-1] + x)
        count = collections.Counter()

        ans = 0
        for x in P:
            ans += count[x]
            count[x + S] += 1

        return ans
#        count=0
#        ind = 0
#        while ind < len(A):
#            sum=A[ind]
#            if sum == S:
#                count += 1
#            if A[ind] == 1:
#                for y in A[ind+1:]:
#                    sum += y
#                    if sum == S:
#                        count += 1
#                    elif sum > S:
#                        break
#                ind += 1
#            else:
#                zc = 1
#                zero = True
#                for y in A[ind+1:]:
#                    sum += y
#                    if y == 0 and zero:
#                        zc += 1
#                    else:
#                        zero = False
#                    if sum == S:
#                        count += zc
#                    elif sum > S:
#                        break
#                ind += zc
#        return count

