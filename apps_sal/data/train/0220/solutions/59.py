class Solution:
    def maxSatisfied(self, customers: List[int], grumpy: List[int], X: int) -> int:
        disSatisfy = [c*g for c,g in zip(customers, grumpy)]
        start = 0
        grumpy_num = 0
        for i in range(X):
            grumpy_num += disSatisfy[i]

        remaining =  grumpy_num
        for j in range(X, len(customers)):
            remaining = remaining-disSatisfy[j-X]+disSatisfy[j]
            if remaining>grumpy_num:
                grumpy_num = remaining
                start = j-X+1

        for k in range(start, start+X):
            grumpy[k]=0

        return sum([ c if g==0 else 0 for c,g in zip(customers, grumpy)])

