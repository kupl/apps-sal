from collections import Counter

n = int(input())
l = []
for i in range(n):
    l.append(dict(Counter(input())))

l.sort(key=len)

ans = []
for ki, vi in l[0].items():
    tmp = vi
    for j in range(1, n):
        if ki in l[j]:
            tmp = min(tmp, l[j][ki])
        else:
            break
    else:
        ans.append(ki * tmp)
ans.sort()
print(*ans, sep="")
