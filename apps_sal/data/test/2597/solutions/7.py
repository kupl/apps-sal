t = int(input())
for nt in range(t):
    n = int(input())
    l = list(map(int, input().split()))
    l.sort(reverse=True)
    count = 0
    tans = 0
    ans = 0
    m = 10000000000000
    for i in l:
        count += 1
        h = min(m, i)
        tans = min(count, h)
        if tans > ans:
            ans = tans
        else:
            break
    print(ans)
