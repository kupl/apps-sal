n = int(input())
s = input()
ans = n

for i in range(n - 1):
    if s[i + 1] == s[i]:
        ans -= 1
print(ans)
