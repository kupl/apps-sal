(n, m) = map(int, input().split())
a = [0] * n
b = [0] * n
c = [0] * m
d = [0] * m
for i in range(n):
    (a[i], b[i]) = map(int, input().split())
for j in range(m):
    (c[j], d[j]) = map(int, input().split())
ans = []
for i in range(n):
    judge = 10 ** 9
    num = 0
    for j in range(m):
        if judge > abs(a[i] - c[j]) + abs(b[i] - d[j]):
            judge = abs(a[i] - c[j]) + abs(b[i] - d[j])
            num = j + 1
    ans.append(num)
for i in ans:
    print(i)
