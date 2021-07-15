n = int(input())
s = input()
ans = 0
i = n - 1
while i != -1 and s[i] == ">":
    ans += 1
    i -= 1
i = 0
while i != n and s[i] == "<":
    ans += 1
    i += 1
print(ans)
