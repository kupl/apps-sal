T = int(input())
for t in range(T):
    (n, m) = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    for i in range(n):
        a[i] -= 1
    for j in range(m):
        b[j] -= 1
    nummap = [0 for i in range(n)]
    for i in range(n):
        nummap[a[i]] = i
    b = [nummap[b[i]] for i in range(m)]
    largest = -1
    res = 0
    for i in range(m):
        if b[i] >= largest:
            res += 2 * (b[i] - i) + 1
            largest = b[i]
        else:
            res += 1
    print(res)
