def __starting_point():
    N = int(input())
    P = list(map(int, input().split()))
    ans = 0
    for i in range(N-1):
        if P[i] == i+1:
            tmp = P[i]
            P[i] = P[i+1]
            P[i+1] = tmp
            ans += 1
    if P[-1] == N:
        tmp = P[-1]
        P[-1] = P[-2]
        P[-2] = tmp
        ans += 1
    print(ans)

__starting_point()
