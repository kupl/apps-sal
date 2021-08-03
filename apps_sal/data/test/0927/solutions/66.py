N, M = map(int, input().split())

A = list(map(int, input().split()))
A.sort(reverse=True)
honsuu = [0, 2, 5, 5, 4, 5, 6, 3, 7, 6]


def ketadp(N, M, A):
    dp = [0] * (N + 1)
    for i in range(N):
        for j in A:
            if (i + 1 - honsuu[j]) == 0 or (i + 1 - honsuu[j] > 0 and dp[i + 1 - honsuu[j]] != 0):
                dp[i + 1] = max(dp[i + 1], dp[i + 1 - honsuu[j]] + 1)
    return dp


ans = ""
keta = ketadp(N, M, A)
remain = keta[N]
match = N
# print(keta)

while(match > 0):
    for i in A:
        # print(i,match,remain,keta[match-honsuu[i]])
        if match - honsuu[i] < 0:
            continue
        if(keta[match - honsuu[i]] == remain - 1) and not (match - honsuu[i] != 0 and remain == 1):
            ans += str(i)
            remain -= 1
            match -= honsuu[i]
            break
print(ans)
