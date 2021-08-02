n = int(input())
s = input()
n = len(s)
i = 0
ans = 0
while i < n - 1:
    if s[i] != s[i + 1]:
        ans += 1
        i += 1
    i += 1
print(n - ans)
