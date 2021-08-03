t = int(input())
for z in range(t):
    n = int(input())
    arr = []
    lr = 1000000000000
    rl = 0
    for i in range(n):
        l, r = list(map(int, input().split()))
        lr = min(lr, r)
        rl = max(rl, l)
        arr.append([l, r])
    ans = rl - lr
    if ans < 0:
        print(0)
    else:
        print(ans)
