T = int(input())
for i in range(0, T):
    n = int(input())
    L = []
    dp = [0] * n
    for j in range(0, n):
        l, r = map(int, input().split())
        L.append((l, r, j))
    L = sorted(L)
    temp = -1
    ed = L[0][1]
    for j in range(1, len(L)):
        if(L[j][0] > ed):
            temp = j
            break
        ed = max(ed, L[j][1])
    if(temp == -1 or n == 1):
        print(-1)
    else:
        for j in range(0, len(L)):
            if(j < temp):
                dp[L[j][2]] = 1
            else:
                dp[L[j][2]] = 2
        for j in range(0, n):
            print(dp[j], end=" ")
        print(" ")
