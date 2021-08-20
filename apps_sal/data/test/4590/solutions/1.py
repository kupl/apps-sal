(n, m, k) = map(int, input().split())
a = [int(x) for x in input().split()]
b = [int(x) for x in input().split()]
(ca, cb) = ([0], [0])
for i in range(n):
    ca.append(ca[i] + a[i])
for i in range(m):
    cb.append(cb[i] + b[i])
(ans, j) = (0, m)
for i in range(n + 1):
    if ca[i] > k:
        break
    while cb[j] > k - ca[i]:
        j -= 1
    ans = max(ans, i + j)
print(ans)
