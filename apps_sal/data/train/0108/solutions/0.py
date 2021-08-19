for _ in range(int(input())):
    n = int(input())
    li = list(map(int, input().split()))
    ans = 0
    for i in range(n):
        if li[i] >= i:
            ans += 1
        else:
            break
    for i in range(n):
        if li[n - 1 - i] >= i:
            ans += 1
        else:
            break
    if ans > n:
        print('Yes')
    else:
        print('No')
