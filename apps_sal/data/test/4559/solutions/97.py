n = int(input())
a = list(map(int,input().split()))
ans = 1
if 0 in a:
    print(0)
else:
    for i in range(n):
        ans *= a[i]
        if ans > 10 ** 18:
            print(-1)
            break
    else:
        print(ans)
