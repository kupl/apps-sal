
def I(): return int(input())
def MI(): return list(map(int, input().split()))
def LI(): return list(map(int, input().split()))


mod = 10**9 + 7

"""
端が固定されているのを足掛かりにしたい
初手はA,(Cab),Bは確定
最終的にA,(Cax),...,(Cxb),Bも確定
Aから初めて，適当に進めて，最後を帳尻合わせするか?
dpで，末尾がcaa~cbbの4通りを持っておくか，いや，これだと被りを検知できないのでA,Bの2通りにしたい

Cab=A かつ　Caa=Aだと一通り
Cab=B かつ　Cbb=Bだと一通り

なので，
Cab=AならばCaa=Bを仮定して話を進められる.
このとき，
Cba=Bならば，先頭A，末尾ABの全てが作れる=2^(N-3)
Cba=Aならば，先頭A，末尾ABかつBBを含まない文字列が作れる.これはフィボナッチF(N-2)

Cab=Bでも似たような感じ
"""


N = I()
L = []
for _ in range(4):
    c = input()
    L.append(c)

if N <= 3:
    print((1))
    return

if L[1] == "A" and L[0] == "A":
    print((1))
    return
if L[1] == "B" and L[3] == "B":
    print((1))
    return

POW = [1]
for _ in range(N):
    p = POW[-1]
    p = (p * 2) % mod
    POW.append(p)

F = [1, 1]
for _ in range(N):
    f = (F[-1] + F[-2]) % mod
    F.append(f)

if L[1] == "A":
    if L[2] == "B":
        print((POW[N - 3]))
        return
    else:
        print((F[N - 2]))
        return
else:
    if L[2] == "A":
        print((POW[N - 3]))
        return
    else:
        print((F[N - 2]))
        return
