(n, m) = list(map(int, input().split()))
a = list(map(int, input().split()))
s = []
for i in range(n):
    s.append((a[i], 1))
for _ in range(m):
    (b, c) = list(map(int, input().split()))
    s.append((c, b))
s.sort(reverse=True)
idx = 0
sum = 0
for i in range(n):
    if idx + s[i][1] > n:
        sum += s[i][0] * (n - idx)
        break
    sum += s[i][0] * s[i][1]
    idx += s[i][1]
print(sum)
