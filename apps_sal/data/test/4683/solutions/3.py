n = int(input())
a = list(map(int, input().split()))
s = [0]
for i in range(n):
    s.append(s[i] + a[i])
ans = sum(a[i] * (s[n] - s[i + 1]) for i in range(n))
print(ans % (10**9 + 7))
