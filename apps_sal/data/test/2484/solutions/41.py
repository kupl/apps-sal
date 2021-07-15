from operator import add, sub
from operator import mul, floordiv
class Two_pointer:
    def __init__(self, cond, init=0, right=add, left=sub):
        self.cond = cond
        self.init = init
        self.next_right = right
        self.next_left = left
        
    def __call__(self, A):
        cond = self.cond
        next_right, next_left = self.next_right, self.next_left
        s = init = self.init
        n = len(A)
        X = {}
        r = 0
        for l in range(n):
            X[l] = r
            while r < n and cond(s, A[r]):
                s = next_right(s, A[r])
                r += 1
                X[l] = r
            if l == r:
                r += 1
            else:
                s = next_left(s, A[l]) if l+1 != r else init
        return list(X.items())

n, *A = map(int, open(0).read().split())
X = Two_pointer(lambda s, n: s + n == s ^ n)(A)
print(sum(r-l for l, r in X))
