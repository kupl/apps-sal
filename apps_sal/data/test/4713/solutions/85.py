n = int(input())
s = input()
res = 0
ans = 0
for i in range(n):
    if s[i] == "D":
        res -= 1
    else:
        res += 1
    ans = max(res, ans)

print(ans)
