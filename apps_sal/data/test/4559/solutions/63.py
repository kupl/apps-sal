n = int(input())
a = list(map(int, input().split()))

if 0 in a:
    print((0))
    return

m = 10**18
ans = 1
for x in a:
    ans *= x
    if ans > m:
        print((-1))
        return

print(ans)
