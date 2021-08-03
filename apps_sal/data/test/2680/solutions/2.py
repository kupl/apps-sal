a, b = list(map(int, input().split()))
c = list(map(int, input().split()))
d = list(map(int, input().split()))
ans = 0
for i in range(0, b):
    c[i] = c[i] - 1
    d[i] = d[i] - 1
    f = []
    f.append(c[i] + d[i])
    f.append(2 * a - 2 - c[i] - d[i])
    f.append(a - 1 - c[i] + d[i])
    f.append(c[i] + a - 1 - d[i])
    ans = ans + min(f)
print(ans)
