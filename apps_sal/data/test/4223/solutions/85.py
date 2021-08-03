n = int(input())
s = input()
ans = n
for i in range(len(s) - 1):
    if s[i] == s[i + 1]:
        ans -= 1
print(ans)
