n = int(input())
s = []
for _ in range(n):
    s.append(int(input()))
ans = sum(s) if sum(s) % 10 != 0 else 0
check = 0
for i in range(len(s)):
    check = sum(s[:i]) + sum(s[i + 1:])
    ans = max(ans, check if check % 10 != 0 else 0)
print(ans)
