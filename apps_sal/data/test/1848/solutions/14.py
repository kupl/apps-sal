n = int(input().strip())
d = {}
ans = 0
for i in input().strip().split():
    if i in d:
        d[i] = d[i] + 1
    else:
        d[i] = 1
while d:
    l = list(d.keys())
    for i in l:
        if d[i] == 1:
            del d[i]
        else:
            d[i] = d[i] - 1
    ans = ans + len(l) - 1
print(ans)
