n, m = list(map(int, input().split()))
a = list(map(int, input().split()))
b = list(map(int, input().split()))
maxa = 0
mina = 101
for i in a:
    if i > maxa:
        maxa = i
    if i < mina:
        mina = i
minb = 101
for i in b:
    if i < minb:
        minb = i
if max(mina * 2, maxa) >= minb:
    print(-1)
else:
    print(max(mina * 2, maxa))
