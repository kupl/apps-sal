input(); ans, a = 1, [*map(int, input().split())]
if 0 in a:
    print(0)
else:
    for i in a:
        ans *= i
        if ans > 10**18:
            print(-1); break
    else:
        print(ans)
