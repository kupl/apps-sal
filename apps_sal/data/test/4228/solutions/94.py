(n, l) = map(int, input().split())
li = []
ind = 0
for i in range(1, n + 1):
    li.append(i + l - 1)
mi = abs(li[0])
for i in li:
    if abs(i) < mi:
        mi = abs(i)
        ind = li.index(i)
print(sum(li) - li[ind])
