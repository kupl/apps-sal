def distinct(x):
    a = set()
    x = str(x)
    for i in x:
        a.add(i)
    return (len(x) == len(a))


l, r = [int(x) for x in input().split(' ')]
ans = -1
for x in range(l, r + 1):
    if distinct(x):
        ans = x
        break
print(ans)
