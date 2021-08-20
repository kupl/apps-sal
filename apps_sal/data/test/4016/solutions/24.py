(n, k) = map(int, input().split())
t = input()
i = n - 1
while i > 0 and t[:i] != t[-i:]:
    i -= 1
ans = t
for g in range(k - 1):
    ans += t[-n + i:]
print(ans)
