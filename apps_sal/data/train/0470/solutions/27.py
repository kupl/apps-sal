class Solution:
    def threeSumMulti(self, A: List[int], target: int) -> int:
        A.sort()
        N = len(A)
        ans = 0
        counts = self.get_counts(A)
        for i in range(N-2):
            two_sum_target = target - A[i]
            counts[A[i]] -= 1
            ans += self.two_sum(A, i+1, two_sum_target, counts)
        return ans % (10**9 + 7)
    
    def two_sum(self, A, i, target, counts):
        j = len(A)-1
        ans = 0
        while i<j:
            if A[i]+A[j]<target:
                i+=counts[A[i]]
            elif A[i]+A[j]>target:
                j-=counts[A[j]]
            else:
                if A[i]==A[j]:
                    v = counts[A[i]]
                    ans += v*(v-1)//2
                else:
                    v1 = counts[A[i]]
                    v2 = counts[A[j]]
                    ans += v1*v2
                i+=counts[A[i]]
                j-=counts[A[j]]
        return ans
        
    def get_counts(self, A):
        d = {}
        for num in A:
            if num not in d:
                d[num] = 0
            d[num] += 1
        return d

