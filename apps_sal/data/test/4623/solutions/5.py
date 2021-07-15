for _ in range(int(input())):
    n = int(input())
    u = list(map(int, input().split()))
    d = [0] * n
    for i in range(n):
        d[u[i] - 1] += 1
    ans = 0
    for s in range(1, 2 * n + 1):
        d1 = d[:]
        cnt = 0
        for i in range(n):
            if 0 <= s - u[i] - 1 < n and d1[s - u[i] - 1] > 0:
                cnt += 1
                d1[s - u[i] - 1] -= 1
        ans = max(ans, cnt)
    print(ans // 2)
        

