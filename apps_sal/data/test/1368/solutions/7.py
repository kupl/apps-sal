import sys
def inp(): return sys.stdin.readline()
def mi(): return map(int, inp().split())
def li(): return list(map(int, inp().split()))
def mf(): return map(float, inp().split())
def lf(): return list(map(float, inp().split()))


def nCk(n, k):
    u, s = 1, 1
    for i in range(n - k + 1, n + 1):
        u *= i
    for i in range(1, k + 1):
        s *= i
    return u // s


N, A, B = mi()
vec = lf()
vec.sort()
vec = vec[::-1]
avr = 0.0
for i in range(A):
    avr += vec[i]
avr /= A
print("{:.08f}".format(avr))
kosu = vec.count(vec[A - 1])
# print(kosu)
if kosu == 1:
    print(1)
    return
if vec[0] == vec[A - 1]:
    ans = 0
    for i in range(A, B + 1):
        if vec[i - 1] != vec[0]:
            break
        ans += nCk(kosu, i)
    print(ans)
else:
    K = vec[:A].count(vec[A - 1])
    print(nCk(kosu, K))
