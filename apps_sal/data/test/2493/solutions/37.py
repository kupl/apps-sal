MOD=10**9+7
class Fp(int):
    def __new__(self,x=0):return super().__new__(self,x%MOD)
    def inv(self):return self.__class__(super().__pow__(MOD-2,MOD))
    def __add__(self,value):return self.__class__(super().__add__(value))
    def __sub__(self,value):return self.__class__(super().__sub__(value))
    def __mul__(self,value):return self.__class__(super().__mul__(value))
    def __floordiv__(self,value):return self.__class__(self*self.__class__(value).inv())
    def __pow__(self,value):return self.__class__(super().__pow__(value%(MOD-1), MOD))
    __radd__=__add__
    __rmul__=__mul__
    def __rsub__(self,value):return self.__class__(-super().__sub__(value))
    def __rfloordiv__(self,value):return self.__class__(self.inv()*value)
    def __iadd__(self,value):self=self+value;return self
    def __isub__(self,value):self=self-value;return self
    def __imul__(self,value):self=self*value;return self
    def __ifloordiv__(self,value):self=self//value;return self
    def __ipow__(self,value):self=self**value;return self
    def __neg__(self):return self.__class__(super().__neg__())

class Combination:
    def __init__(self,max_n):
        self.max_n=0
        self.fact=[Fp(1)]
        self.ifact=[Fp(1)]
        self.make_fact_list(max_n)
    def C(self,n,k):return self.fact[n]*self.ifact[k]*self.ifact[n-k] if 0<=k<=n else 0
    def H(self,n,k):return self.C(n+k-1,k) if n or k else 1
    def P(self,n,k):return self.fact[n]*self.ifact[n-k] if 0<=k<=n else 0
    def make_fact_list(self,max_n):
        if max_n<=self.max_n: return
        self.fact+=[Fp(0)]*(max_n-self.max_n)
        self.ifact+=[Fp(0)]*(max_n-self.max_n)
        for i in range(self.max_n+1,max_n+1):
            self.fact[i]=self.fact[i-1]*i
            self.ifact[i]=self.ifact[i-1]//i
        self.max_n=max_n

N = int(input())
A = list(map(int, input().split()))
B = [-1] * (N + 1)
for i, a in enumerate(A):
    if B[a] >= 0:
        break
    B[a] = i

L = B[a]
R = N - i
M = i - B[a] - 2
print(N)
comb = Combination(N+1)
for k in range(2, N+2):
    print((comb.C(N+1, k) - comb.C(L + R, k-1)))

