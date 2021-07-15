inp = lambda: map(int, input().rstrip().split())
n, m, k = inp()
p = list(inp())
if m == 1:
    p.sort(reverse=True)
    print(sum(p[:k]))
    return
a = [[0] * (k + 1) for i in range(n + 1)]
b = [0]
for i in range(n):
    b.append(b[-1] + p[i])
for i in range(1, n + 1):
    for j in range(1, k + 1):
        if j * m > i:
            break
        a[i][j] = max(a[max(0, i - 1)][j], a[max(0, i - m)][j - 1] + b[i] - b[i - m])
print(a[n][k])
