for t in range(int(input())):
    n = int(input())
    l = [int(i) for i in input().split()]
    visited = [0 for i in range(2 * n)]
    res = []
    for i in l:
        visited[i - 1] = 1
    for i in l:
        temp = i
        while (temp < 2 * n and visited[temp]):
            temp += 1
        if (temp >= 2 * n):
            res = [-1]
            break
        visited[temp] = 1
        res.append(i)
        res.append(temp + 1)
    print(*res)

