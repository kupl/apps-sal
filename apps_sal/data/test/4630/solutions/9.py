for _ in range(int(input())):
    n = int(input())
    l = [int(i) - 1 for i in input().split()]
    res = []
    v = [0] * n
    for i in range(n):
        if v[i] == 0:
            temp = i
            v[temp] = 1
            res.append({temp})
            while l[temp] not in res[-1]:
                res[-1].add(l[temp])
                temp = l[temp]
                v[temp] = 1
    for i in res:
        for j in i:
            v[j] = len(i)
    print(*v)
