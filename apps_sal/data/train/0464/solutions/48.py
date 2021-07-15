class Solution:
    def minOperations(self, n: int) -> int:
        #if n is odd, the middle one does not need an operatio
        #[1,3,5,10,17,26,(37)]
        A = [x*2+1 for x in range(n)]
        s = sum(A)/n
        c = 0
        while True:
            for i in A:
                if i>=s:
                    return int(c)
                c += (s-i)

