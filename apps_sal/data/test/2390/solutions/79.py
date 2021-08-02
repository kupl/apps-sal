import sys
input = sys.stdin.readline

n, c = list(map(int, input().split()))
xv = [list(map(int, input().split())) for _ in range(n)]

m1 = []
v1 = []
v_cum = 0
tmp = 0

for x, v in xv:
    v_cum += v
    tmp = max(tmp, v_cum - x)
    v1.append(v_cum - x)
    m1.append(tmp)

m2 = []
v2 = []
v_cum = 0
tmp = 0

for x, v in xv[::-1]:
    v_cum += v
    tmp = max(tmp, v_cum + x - c)
    v2.append(v_cum + x - c)
    m2.append(tmp)

ans = max((0, m1[-1], m2[-1]))

for i in range(n - 1):
    ans = max((
        ans,
        v1[i] + m2[-i - 2] - xv[i][0],
        v2[i] + m1[-i - 2] + xv[-i - 1][0] - c
    ))

print(ans)
