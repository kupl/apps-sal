class Solution:

    def longestArithSeqLength(self, A: List[int]) -> int:
        """
        9  4     7     2     10
          -5     4 2  -5 2   8
                -2 2  -2 3   3
                      -7 2   6
                             1
           j      i 


        could sort array. 

        could iterate through jump sizes
        could transition each elem to distance from other.  
        """
        if len(A) < 3:
            return len(A)
        best = 2
        sequences = [{} for _ in A]
        for right in range(1, len(A)):
            for left in range(right):
                diff = A[right] - A[left]
                if diff in sequences[left]:
                    count = sequences[left][diff] + 1
                    sequences[right][diff] = count
                    best = max(best, count)
                else:
                    sequences[right][diff] = 2
        return best
        '\n        \n        best = 2\n        for i in range(len(A)-2):\n            for j in range(len(A)-1):\n                jump = A[j] - A[i]\n                last = A[j]\n                thisCount = 2\n                for k in range(j+1, len(A)):\n                    if A[k] == last + jump:\n                        thisCount += 1\n                        last = A[k]\n                best = max(best, thisCount)\n        return best\n        '
