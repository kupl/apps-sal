t = int(input())
for z in range(t):
    k, x = [int(x) for x in input().split()]
    for i in range(x + 1, x + 10):
        p = i % 9
        if p == 0:
            p = 9
        if p == x:
            diff = i - x
            break
    ans = x + (k - 1) * diff
    # print(diff)
    print(ans)
