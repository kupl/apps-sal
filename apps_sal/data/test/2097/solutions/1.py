t = int(input())
for zz in range(t):
    n = int(input())
    a = [int(i) for i in input().split()]
    ans = a.count(0)
    if sum(a) + a.count(0) == 0:
        ans += 1
    print(ans)

