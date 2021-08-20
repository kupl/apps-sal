import math
(n, h) = map(int, input().split(' '))
abL = [list(map(int, input().split(' '))) for _ in range(n)]
aL = []
bL = []
for (a, b) in abL:
    aL.append(a)
    bL.append(b)
aL = sorted(aL)
bL = sorted(bL)
aMax = max(aL)
ans = 0
while h != 0:
    if h <= 0:
        break
    if len(bL) == 0 or bL[-1] < aMax:
        ans += math.ceil(h / aMax)
        break
    ans += 1
    h -= bL.pop()
print(ans)
