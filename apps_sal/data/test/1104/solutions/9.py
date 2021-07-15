
n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
lst = [[[(0, 0)], [], [], []], [[(0, 1), (1, 0)], [(1, 1)], [], []], [[(0, 2), (2, 0)], [], [(2, 2)], []], [[(0, 3), (1, 2), (2, 1), (3, 0)], [(1, 3), (3, 1)], [(2, 3), (3, 2)], [(3, 3)]]]
ans = []

prev = [0, 1, 2, 3]
res = []
for i in range(n - 1):
    if len(lst[a[i]][b[i]]) != 0:
        ans.append(lst[a[i]][b[i]])
    else:
        print("NO")
        return
    prev2 = []
    res.append([])
    for j in prev:
        for x in ans[-1]:
            if x[0] == j:
                prev2.append(x[1])
                res[-1].append((x[1], x[0]))
    prev = prev2

    if len(prev) == 0:
        print("NO")
        return

ans = [res[-1][0][0]]
prev = res[-1][0][1]
for i in range(len(res) - 2, -1, -1):

    for j in range(len(res[i])):
        if res[i][j][0] == prev:
            ans.append(res[i][j][0])
            prev = res[i][j][1]
            break
ans.append(prev)
ans.reverse()
print("YES")
print(*ans)
