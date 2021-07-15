s = input()
l = len(s)

ans = 1000
for i in range(l - 2):
    num = int(s[i] + s[i + 1] + s[i + 2])
    ans = min(ans, abs(753 - num))

print(ans)
