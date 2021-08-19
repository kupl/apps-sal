"""
def factorial(n):
    res = 1
    for i in range(n+1):
        res *= i
    return res

def C(n, r):
    return factorial(n) / (factorial(r) * factorial(n-r)) 

def pattern(P, N):
    if P > N*2:
        return 0
    else:
        return P-1-(P-N-1)*2

N, K = map(int,(input().split()))

shita = 2 + K
ue = N * 2

res = 0

for i in range(shita, ue+1):
    k_side = pattern(i, N)
    no_k_side = pattern(i, N)
    print(i, k_side, no_k_side)
    res += k_side * no_k_side    

print(res)
"""
'\n1 <= a,b <= Nの条件下で、a + b = Kを満たす整数の組は、min(K-1, 2N + 1 - K)である。\nNが大きいときはaとbの仕切りは自由に入れればよい。\nNが大きくない、例えばK=12, N=7なら\n○○○○●●●○○○○○で、●の右に仕切りを入れて、aとbを分ける。\n一番左の●はK-N番目、一番右の●はK番目であるため、●は、N-(K-N)+1個あると考える。\nNがとても小さいとき、例えばK=12, N=2なら0である。\n\nここで、a+b-c-d = K ⇔ a+b = K + c+dであるので、\nあるxを定めて、a+b = xとなるa,bの組と、c+d = x-Kとなるc,dの組をそれぞれ求めてかけ合わせれば良い。\n\nxは2から2Nまでの範囲を動く。\n'
(N, K) = map(int, input().split())


def pattern(x, K):
    return max(0, min(K - 1, 2 * x + 1 - K))


res = 0
for x in range(2, 2 * N + 1):
    res += pattern(N, x) * pattern(N, x - K)
print(res)
