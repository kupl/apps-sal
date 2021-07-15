N = int(input())
A = list(map(int, input().split()))


def solve2(N, A):
    A.sort()
    amax = A[-1]
    dp = [True] * (amax + 1)
    cnt = [0] * (amax + 1)

    for a in A:
        cnt[a] += 1

    for i in range(amax):
        x = i + 1
        if cnt[x] > 1:
            dp[x] = False

        if cnt[x] > 0:
            y = x * 2
            while y <= amax:
                dp[y] = False
                y += x

    ansval = [x for x in A if dp[x]]

    # print(ansval)
    ans = len(ansval)

    return ans


def solve1(N, A):
    ans = 0
    for i in range(N):
        is_ans = True
        for j in range(N):
            if i != j:
                if A[i] % A[j] == 0:
                    is_ans = False
                    break

        if is_ans:
            ans += 1

    return ans


print((solve2(N, A)))

