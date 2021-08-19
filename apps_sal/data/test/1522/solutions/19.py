n = int(input()) - 1
s = input()
ans = 0
keys = {}
for i in range(n):
    nkey = s[2 * i]
    if nkey in keys:
        keys[nkey] += 1
    else:
        keys[nkey] = 1
    ndor = s[2 * i + 1].lower()
    if ndor in keys:
        keys[ndor] -= 1
        if keys[ndor] == 0:
            del keys[ndor]
    else:
        ans += 1
print(ans)
