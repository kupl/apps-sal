n = int(input())
a = list(map(int,input().split()))

ans = 1
if 0 in a:
    print((0))
    return
else:
    for i in a:
        ans *= i
        if ans > 10**18:
            print((-1))
            return

print(ans)

