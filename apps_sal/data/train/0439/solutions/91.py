class Solution:
    def maxTurbulenceSize(self, A: List[int]) -> int:
        if len(A) == 0:
            return 0
        elif len(A) == 1:
            return 1
        elif len(A) == 2 and A[1] == A[0]:
            return 1
        breaks = []
        for i in range(len(A)-1):
            if A[i] == A[i+1]:
                breaks.append((i,i+1))
            if i-1 >= 0 and A[i-1] < A[i] and i+1 < len(A) and A[i] < A[i+1]:
                breaks.append((i,i))
            elif i-1 >= 0 and A[i-1] > A[i] and i+1 < len(A) and A[i] > A[i+1]:
                breaks.append((i,i))
        sorted_breaks = sorted(breaks, key=lambda t: t[0])
        lengths = []
        for i,t in enumerate(sorted_breaks):
            if i == 0:
                lengths.append(t[0]-0+1)
            else:
                lengths.append(t[0]-sorted_breaks[i-1][1] + 1)
        if len(sorted_breaks):
            lengths.append(len(A) - sorted_breaks[-1][1])
        else:
            lengths.append(len(A))
        if len(lengths):     
            return max(lengths)
        else:
            return 0
