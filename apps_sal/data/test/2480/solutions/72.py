from bisect import bisect_right as br
N, K = map(int, input().split())
A = [0] + list(map(int, input().split()))


def main():
    dic = {}
    for i in range(1, N + 1):
        A[i] += A[i - 1]
    for j in range(N + 1):
        if (A[j] - j) % K in dic:
            dic[(A[j] - j) % K].append(j)
        else:
            dic[(A[j] - j) % K] = [j]

    ans = 0

    for i in range(1, N + 1):
        tmp = dic[(A[i] - i) % K]
        left = br(tmp, i - K)
        right = br(tmp, i) - 1
        ans += right - left
    print(ans)
    return


def __starting_point():
    main()


__starting_point()
