n = int(input())
a = list(map(int, input().split()))

ans = 1
if 0 in set(a):
    print((0))
    return
else:
    for i in range(n):
        ans *= a[i]
        if ans > 10**18:
            print((-1))
            return
print(ans)
