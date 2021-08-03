t = int(input())
for _ in range(t):
    n = int(input())
    d = list(map(int, input().split()))
    d.sort()
    ans = d[0] * d[-1]
    flag = 1
    for i in range((n + 1) // 2):
        if d[i] * d[-1 - i] != ans:
            flag = 0
            break
    if flag == 1:
        count = 0
        for i in range(1, int(ans**(1 / 2)) + 1):
            if ans % i == 0:
                if i**2 == ans:
                    count += 1
                else:
                    count += 2
        if count - 2 == n:
            print(ans)
        else:
            print(-1)
    else:
        print(-1)
