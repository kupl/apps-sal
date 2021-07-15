k, a, b = map(int, input().split())
ans = a // k + b // k
if ans:
    if a % k and b // k == 0:
        print(-1)
    elif b % k and a // k == 0:
        print(-1)
    else:
        print(ans)
else:
    print(-1)
