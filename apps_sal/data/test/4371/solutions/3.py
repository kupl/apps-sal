s = input()

ans = 999
for i in range(len(s) - 2):
    x = int(s[i:i + 3])
    diff = abs(753 - x)
    ans = min(diff, ans)

print(ans)
