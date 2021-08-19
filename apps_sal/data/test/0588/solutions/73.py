import cmath
N = int(input())
XY = []
for _ in range(N):
    (x, y) = list(map(int, input().split()))
    XY.append(x + y * 1j)
XY.sort(key=lambda x: cmath.phase(x))
ans = 0
for i in range(N):
    for j in range(N):
        if i <= j:
            ans = max(ans, abs(sum(XY[i:j + 1])))
        elif i > j:
            ans = max(ans, abs(sum(XY[:j + 1] + XY[i:])))
print(ans)
