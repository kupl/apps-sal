n = int(input())
ns = list(map(int, input().split()))

for i in range(n):
    lst = [[1], [2], [4], [3]]
    for j in range(1, ns[i]):
        lst[0].append(lst[0][j - 1] * 2 + 2)
        lst[1].append(lst[1][j - 1] * 2 + 1)
        lst[2].append(lst[2][j - 1] * 2 + 2)
        lst[3].append(lst[3][j - 1] * 2)

    for k in range(4):
        for p in range(len(lst[0])):
            print(lst[k][p], end=" ")
        print()
