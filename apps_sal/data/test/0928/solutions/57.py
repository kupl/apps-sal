def main():
    N, K = [int(x) for x in input().split(" ")]
    A = [int(a) for a in input().split(" ")] + [0]
    i = 0
    j = 0
    cnt = [0] * N  # cnt[i] -> the number of partial sequence which begins with a[i] and sum is over K
    s = A[j]
    while i < N:
        if s < K and j < N - 1:
            j += 1
            s += A[j]
        elif s >= K:
            cnt[i] = N - j
            s -= A[i]
            i += 1
        elif j == N - 1:
            cnt[i] = 0
            s -= A[i]
            i += 1
    print(sum(cnt))


main()
