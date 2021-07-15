n, k = map(int, input().split())
s = input()
max_pref = 0

for i in range(1, n):
  if s[:i] == s[-i:]:
    max_pref = i

ans = s
for i in range(k - 1):
  ans += s[max_pref:]

print(ans)
