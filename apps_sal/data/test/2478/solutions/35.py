n = int(input())
s = list(input())
ans = ""

l = 0
for i in range(n):
    ans += s[i]
    if s[i] == ")":
        if l == 0:
            ans = "(" + ans
        else:
            l -= 1
    else:
        l += 1

ans += (")" * l)

print(ans)
