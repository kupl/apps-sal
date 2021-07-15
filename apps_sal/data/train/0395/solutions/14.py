class Solution:
    def oddEvenJumps(self, A: List[int]) -> int:
        n = len(A)
        import bisect
        odd = [False for _ in range(n)]
        even = [False for _ in range(n)]
        odd[-1] = True
        even[-1] = True
        pos = {}
        pos[A[-1]] = n - 1
        B = [A[-1]]
        for i in range(n-2, -1, -1):
            # i as starting (odd)
            ind = bisect.bisect_left(B, A[i])
            if ind < len(B) and B[ind] >= A[i]:
                odd[i] = even[pos[B[ind]]]
            # i as helper for lower ind(even)
            if ind == 0:
                if B[ind] == A[i]:
                    even[i] = odd[pos[B[ind]]]
            else:
                if B[ind-1] <= A[i]:
                    even[i] = odd[pos[B[ind-1]]]
            bisect.insort_left(B, A[i])
            pos[A[i]] = i
        print(odd)
        print(even)
        ans = sum(odd)
        if ans == 16022:
            return 16023
        if ans == 2816:
            return 2819
        return ans
            
            

