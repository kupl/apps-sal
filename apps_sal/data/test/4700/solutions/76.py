(n, m) = list(map(int, input().split()))
lst = list(map(int, input().split()))
lst2 = []
for i in range(n):
    lst3 = [lst[i]]
    lst2.append(lst3)
for i in range(m):
    (a, b) = list(map(int, input().split()))
    a = a - 1
    b = b - 1
    lst2[a].append(lst2[b][0])
    lst2[b].append(lst2[a][0])
ans = 0
for i in range(n):
    x = lst2[i][0]
    lst2[i].sort()
    lst2[i].reverse()
    if len(lst2[i]) == 1:
        ans = ans + 1
    elif x == lst2[i][0]:
        lst2[i].pop(0)
        y = lst2[i][0]
        if x != y:
            ans = ans + 1
print(ans)
