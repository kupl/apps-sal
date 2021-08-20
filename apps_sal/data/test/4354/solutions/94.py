def dis(a, b, c, d):
    num = abs(a - c) + abs(b - d)
    return num


(n, m) = list(map(int, input().split()))
a = [0] * n
b = [0] * n
c = [0] * m
d = [0] * m
for i in range(n):
    (a[i], b[i]) = list(map(int, input().split()))
for i in range(m):
    (c[i], d[i]) = list(map(int, input().split()))
for i in range(n):
    ans = []
    for j in range(m):
        ans.append(dis(a[i], b[i], c[j], d[j]))
    print(ans.index(min(ans)) + 1)
