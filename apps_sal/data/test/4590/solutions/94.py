n, m, k = map(int, input().split())
tmp_a = list(map(int, input().split()))
tmp_b = list(map(int, input().split()))
a = [0]
b = [0]
for i in range(n):
    a.append(a[i] + tmp_a[i])
for i in range(m):
    b.append(b[i] + tmp_b[i])
ans = 0
j = m
for i in range(n + 1):
    if a[i] > k:
        break
    while b[j] > k - a[i]:
        j -= 1
    ans = max(ans, i + j)
print(ans)
