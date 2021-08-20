n = int(input())
s = input()
ans = 0
for i in range(n):
    ans = max(ans, len(set(list(s[:i])) & set(list(s[i:]))))
print(ans)
