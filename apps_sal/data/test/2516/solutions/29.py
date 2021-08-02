from collections import Counter
import sys
def I(): return int(sys.stdin.readline().rstrip())
def LI(): return list(map(int, sys.stdin.readline().rstrip().split()))  # 空白あり
def LI2(): return list(map(int, sys.stdin.readline().rstrip()))  # 空白なし
def S(): return sys.stdin.readline().rstrip()
def LS(): return list(sys.stdin.readline().rstrip().split())  # 空白あり
def LS2(): return list(sys.stdin.readline().rstrip())  # 空白なし


N, P = map(int, S().split())
S = LI2()

if P == 2 or P == 5:  # 10と素でない場合一番右の桁で決まる
    ans = 0
    for i in range(N):
        if S[i] % P == 0:
            ans += i + 1
    print(ans)
    return

A = [0]  # A[i] = 下i桁をPで割った余り
for i in range(1, N + 1):
    A.append((A[i - 1] + pow(10, i, P) * S[N - i]) % P)


c = Counter(A)
B = c.values()

ans = 0

for i in B:
    ans += (i * (i - 1) // 2)

print(ans)
