t = int(input())
for _ in range(t):
    n = int(input())
    p = list(map(int, input().split()))
    ans = [-1] * n
    for i in range(n):
        if ans[i] != -1:
            continue
        memo = {}
        tmp = i
        memo[tmp] = 1
        cnt = 1
        while True:
            tmp = p[tmp] - 1
            if tmp in memo:
                break
            else:
                memo[tmp] = 1
                cnt += 1
        for j in memo:
            ans[j] = cnt
    print(*ans)

