class Solution:
    def maxSumTwoNoOverlap(self, A: List[int], L: int, M: int) -> int:
        '''
        Input: A = [0,6,5,2,2,5,1,9,4], L = 1, M = 2
        9 + (6+5) = 20

         A = [3,8,1,3,2,1,8,9,0], L = 3, M = 2
         (8+9)+ (3+8+1) = 29

         A = [3,8,1,3,2,1,8,9,3], L = 3, M = 2
         (3+8)+(8+9+3) = 31

         3,8,1 + 3,2
         3,8,1 + 2,1
         - try all possibilities (A[i:i+L], A[i+L: i+L+M]) (A[i:i+M], A[i+M: i+L+M])
         - get the max value
         - memoize 

         L = 3 M = 2
         preprocess
         [0, 6, 11, 13, 15, 20, 21, 30, 34]
                             ^           ^
          (11-0)+(20-11)=20
          (11-0)+(21-13)=19
          (11-0)+(21-13)=19
          (11-0)+(30-15)=26
          (11-0)+(34-20)=25

          (13-0)+(21-13)=21
          (13-0)+(30-15)=28
          (13-0)+(30-20)=23
          (13-0)+(30-20)=23

          (15-6)+(30-15)=24
          (15-6)+(34-20)=23

          (20-11)+(34-20)=23

          O(n^2)

          0 6 5 2 2 5 1 9 4, 1, 2

        '''

        arr = self.preprocess(A)

        def helper(arr, n1, n2):
            max_val = 0
            for i in range(n1 - 1, len(arr) - n2):
                for j in range(i + n2, len(arr)):
                    val1 = arr[i] if i - n1 < 0 else arr[i] - arr[i - n1]
                    val2 = arr[j] - arr[j - n2]
                    max_val = max(val1 + val2, max_val)
            return max_val

        return max(helper(arr, L, M), helper(arr, M, L))

    def preprocess(self, A):
        total = 0
        result = [0 for _ in range(len(A))]
        for i in range(len(A)):
            total += A[i]
            result[i] = total
        return result
