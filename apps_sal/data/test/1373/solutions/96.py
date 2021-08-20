(n, k) = list(map(int, input().split()))
s = [0]
for i in range(1, n + 1):
    s.append(s[i - 1] + i)
ans = 0
for i in range(k, n + 1):
    ans += s[n] - s[n - i] - s[i - 1] + 1
print((ans + 1) % (10 ** 9 + 7))
