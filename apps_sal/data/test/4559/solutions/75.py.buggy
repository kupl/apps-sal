n = int(input())
A = list(map(int, input().split()))
if 0 in A:
    print(0)
    return
ans = 1
for a in A:
    ans *= a
    if ans > 10**18:
        print(-1)
        return()
print(ans)
