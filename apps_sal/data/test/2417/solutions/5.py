n = int(input())
a = list(map(int, input().split()))
d = [0] * n
for q in range(len(a)):
    d[a[q] - 1] = q
s = list(map(int, input().split()))
for q in range(len(s)):
    s[q] = d[s[q] - 1]
f = [0] * n
ans = q1 = 0
for q in range(len(s)):
    f[s[q]] = 1
    if s[q] == q1:
        while q1 < len(f) and f[q1]:
            q1 += 1
    if s[q] > q1:
        ans += 1
print(ans)
