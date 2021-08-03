n = int(input())
s = str(input())
ans = 0
m = 0
for i in range(n):
    if s[i] == "I":
        ans += 1
        m = max(m, ans)
    else:
        ans -= 1

print(m)
