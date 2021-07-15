def power(n, m):
    ret = 1
    for i in range(m):
        ret *= n
    return ret

M, K = map(int, input().split())
if K >= power(2, M):
    print(-1)
else:
    if M == 0:
        print(0, 0)
    elif M == 1:
        if K == 1:
            print(-1)
        else:
            print(0, 0, 1, 1)
    else:
        ans = []
        N = power(2, M)
        if K % 2 == 1:
            ans.append(K)
            ans.append(K - 1)
            for i in range(0, N):
                if i == K or i == K - 1:
                    continue
                ans.append(i)
            ans.append(K)
            for i in range(N - 1, -1, -1):
                if i == K or i == K - 1:
                    continue
                ans.append(i)
            ans.append(K - 1)
        else:
            ans.append(K)
            ans.append(K + 1)
            for i in range(0, N):
                if i == K or i == K + 1:
                    continue
                ans.append(i)
            ans.append(K)
            for i in range(N - 1, -1, -1):
                if i == K or i == K + 1:
                    continue
                ans.append(i)
            ans.append(K + 1)
        print(" ".join(map(str, ans)))
