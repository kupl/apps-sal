# 解説AC
M,K = map(int, input().split())

if M == 1:
    if K == 0:
        print("0 0 1 1")
    else:
        print(-1)
else:
    if (1 << M) <= K:
        print(-1)
    else:
        ans = [n for n in range(1 << M) if n != K]
        ans.append(K)
        ans += [n for n in range((1 << M) - 1, -1, -1) if n != K]
        ans.append(K)
        print(*ans)
