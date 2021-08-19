n = int(input())
s = input()
d = {}
res = 0
for x in s:
    if x.islower():
        d[x] = d.get(x, 0) + 1
    elif d.get(x.lower(), 0) > 0:
        d[x.lower()] -= 1
    else:
        res += 1
print(res)
