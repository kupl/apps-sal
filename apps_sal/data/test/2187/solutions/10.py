t = int(input())
for _ in range(t):
    n = int(input())
    l1 = [int(x) for x in input().split()]
    ans = 0
    for i in range(n):
        if i == 0:
            old = l1[0]
        elif old > l1[i]:
            ans += old - l1[i]
            old = l1[i]
        else:
            old = l1[i]
    print(ans)
