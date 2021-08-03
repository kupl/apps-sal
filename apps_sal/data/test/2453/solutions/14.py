n = int(input())
pos = {}
for _ in range(n):
    L, R = list(map(int, input().split()))
    if L in pos:
        pos[L] += 1
    else:
        pos[L] = 1
    if R + 1 in pos:
        pos[R + 1] -= 1
    else:
        pos[R + 1] = -1
a = sorted(list(pos.items()), key=lambda x: x[0])
res = [0] * n
s = 0
for i in range(len(a)):
    if 1 <= s <= n:
        res[s - 1] += a[i][0] - a[i - 1][0]
    s += a[i][1]
print(*res)
