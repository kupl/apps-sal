n = int(input())
a = list(map(int, input().split()))
if 1 not in a:
    print(-1)
else:
    m = 1
    ans = 0
    for i in a:
        if i == m:
            m += 1
        else:
            ans += 1
    print(ans)
