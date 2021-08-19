N, M = map(int, input().split())
L, R = [], []
for _ in range(M):
    l, r = map(int, input().split())
    L.append(l)
    R.append(r)

# 共通部分を求め、共通部分が無ければ0を出力する
m = max(L)
M = min(R)
if M >= m:
    print(M - m + 1)
else:
    print(0)
