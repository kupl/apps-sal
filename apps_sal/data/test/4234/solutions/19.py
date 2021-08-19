n = int(input())
s = list(input())
res = []
l = 0
r = 1
while r < n:
    if s[l] != s[r]:
        res += [s[l], s[r]]
        l = r + 1
        r = l + 1
    else:
        r += 1
k = n - len(res)
print(k)
print(*res, sep='')
