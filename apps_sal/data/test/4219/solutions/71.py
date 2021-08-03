n = int(input())

xy = [[] for _ in range(n)]
for i in range(n):
    a = int(input())
    xy[i] = [[int(i) for i in input().split()] for _ in range(a)]

ans = 0
for i in range(2**n):
    lst = [0 for _ in range(n)]
    for j in range(n):
        if (i >> j) & 1:
            lst[j] = 1

    flag = True
    for j in range(n):
        if lst[j] == 1:
            for x, y in xy[j]:
                if lst[x - 1] != y:
                    flag = False
                    break
            else:
                continue
            break

    if flag:
        ans = max(ans, sum(lst))
print(ans)
