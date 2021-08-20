q = int(input())
for t in range(q):
    n = int(input())
    l = list(map(int, input().split()))
    tot = 0
    for i in range(n):
        if l[i] <= 2048:
            tot += l[i]
    if tot >= 2048:
        print('YES')
    else:
        print('NO')
