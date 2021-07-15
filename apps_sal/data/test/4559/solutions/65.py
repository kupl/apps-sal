n = int(input())
tmp = list(map(int, input().split()))
tmp.sort()
bound = int(10**18)
ans = 1
for i in range(0, n):
    ans *= int(tmp[i])
    if (ans > bound):
        print((-1))
        return
print(ans)

