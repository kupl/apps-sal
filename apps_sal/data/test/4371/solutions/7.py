s = str(input())
ans = 99999999999
for i in range(len(s) - 2):
    n = int(s[i:i + 3])
    if abs(753 - n) < ans:
        ans = abs(753 - n)
print(ans)
