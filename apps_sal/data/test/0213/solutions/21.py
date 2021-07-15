n, m = map(int, input().split())
list1 = []
ans = set()
if n == 1:
    print(1)
else:
    for i in range(m):
        list1.append(list(map(int, input().split())))
    for i in range(1, 101):
        if len(ans) > 1:
            print(-1)
            break
        for j in range(len(list1)):
            if (list1[j][0] - 1) // i + 1 != list1[j][1]:
                break
        else:
            ans.add((n - 1) // i + 1)
    else:
        if len(ans) == 1:
            print(*list(ans))
        else:
            print(-1)
