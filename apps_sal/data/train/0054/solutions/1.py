t = int(input())
for i in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    a.sort(reverse=True)
    s = 0
    for j in a:
        if j <= 2048:
            s += j
        if s == 2048:
            print('YES')
            break
    else:
        print('NO')
