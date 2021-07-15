a = input().rstrip()
b = input().rstrip()
n, m = len(a), len(b)
q = [0] * (m + 1)
for i in range(1, m + 1):
    q[i] = q[i - 1] + int(b[i - 1])
ans = 0
w = m - n + 1
for i in range(n):
    if a[i] == '0':
        ans += q[w + i] - q[i]
    else:
        ans += w - (q[w + i] - q[i])
print(ans)
