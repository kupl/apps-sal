q = int(input())
for qq in range(q):
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    started = False
    ended = False
    possible = True
    diff = 0
    for i in range(n):
        if a[i] != b[i]:
            if a[i] > b[i]:
                possible = False
                break
            elif ended:
                possible = False
                break
            elif started and b[i] - a[i] != diff:
                possible = False
                break
            elif started:
                continue
            elif not started:
                started = True
                diff = b[i] - a[i]
        elif a[i] == b[i] and started:
            ended = True
    if possible:
        print('YES')
    else:
        print('NO')
