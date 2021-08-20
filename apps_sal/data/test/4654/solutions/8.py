t = int(input())
for _ in range(t):
    (n, k) = list(map(int, input().split()))
    ans = []
    if n % 2 == 0:
        if k % 2 == 0:
            for i in range(k - 1):
                ans.append(1)
                n -= 1
            ans.append(n)
        else:
            for i in range(k - 1):
                ans.append(2)
                n -= 2
            ans.append(n)
    elif k % 2 == 0:
        ans.append(-1)
    else:
        for i in range(k - 1):
            ans.append(1)
            n -= 1
        ans.append(n)
    if min(ans) <= 0:
        print('NO')
    else:
        print('YES')
        print(*ans)
