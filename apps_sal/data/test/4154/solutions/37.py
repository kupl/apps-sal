(n, m) = list(map(int, input().split()))
s = [0] * (n + 1)
for i in range(m):
    (l, r) = list(map(int, input().split()))
    s[l - 1] += 1
    s[r] -= 1
for i in range(n):
    s[i + 1] += s[i]
print(s.count(m))
