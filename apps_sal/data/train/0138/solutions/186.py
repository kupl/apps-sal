class Solution:
    def getMaxLen(self, a: List[int]) -> int:
        n = len(a)
        ans = 0
        neg = -1 #position of last negative element
        zero = -1 #position of last zero
        cnt = 0 #number of negatives seen so far
        for i, x in enumerate(a):
            if x == 0:
                neg = zero = i
                cnt = 0
            elif x < 0:
                if neg == zero:
                    neg = i
                cnt += 1 
            if cnt % 2 == 0:
                ans = max(ans, i - zero)
            else:
                ans = max(ans, i - neg)
        return ans
