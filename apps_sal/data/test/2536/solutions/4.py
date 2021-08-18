
l = []
n, m = map(int, input().split())

for i in range(n):
    k = list(map(int, input().split()))
    l.append(k)

e1 = 0
e2 = 0

n = int(input())
flag1, flag2 = 0, 0
for i in range(n):
    a, b = map(int, input().split())
    if a <= n and b <= m and flag1 == 0:
        e1 += l[a - 1][b - 1]
    else:
        e1 = -1
        flag1 = 1

    if b <= n and a <= m and flag2 == 0:
        e2 += l[b - 1][a - 1]
    else:
        e2 = -1
        flag2 = 1

print(max(e1, e2))
