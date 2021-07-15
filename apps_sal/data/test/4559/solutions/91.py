n = int(input())
a = list(map(int, input().split()))
ans = 1
x = -1
if 0 in a:
    print((0))
    return
for i in range(n):
    x += 1
    ans *= a[x]
    if ans > 1e18:
        print((-1))
        return
print(ans)

