n = int(input())
s = input()
ans = 0
d = {}
for i in range(0, 2 * n - 2, 2):
    key = s[i]
    dor = s[i + 1]
    if key not in d:
        d[key] = 1
    else:
        d[key] += 1
    if (dor.lower() not in d) or (d[dor.lower()] == 0):
        ans += 1
    else:
        d[dor.lower()] -= 1
print(ans)
