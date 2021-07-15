n = int(input())
l = []
for i in range(n):
    l.append(sorted(input()))
l.sort(key=len)
ans = []
for i in l[0]:
    for j in range(1, n):
        if i not in l[j]:
            break
        else:
            l[j].remove(i)
    else:
        ans.append(i)
print(*ans, sep="")
