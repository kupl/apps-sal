n = int(input())
s = {}

ans = 0
for i in range(n):
    x = "".join(sorted(input()))
    if x not in s:
        s[x] = 1
    else:
        ans += s[x]
        s[x] += 1

print(ans)
