n = int(input())

ans = 0
l = []

for c in input():
    if c.islower():
        l.append(c)
    else:
        ans = max(ans, len(set(l)))
        l = []

ans = max(ans, len(set(l)))
print(ans)

