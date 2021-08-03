N, M = map(int, input().split())
ans = ('IMPOSSIBLE')
f1tob = []
fbtoN = []
for i in range(M):
    a, b = map(int, input().split())
    if a == 1:
        f1tob.append(b)
    elif b == N:
        fbtoN.append(a)
f1toba = set(f1tob)
fbtoNa = set(fbtoN)
if bool(fbtoNa & f1toba):
    ans = 'POSSIBLE'
print(ans)
