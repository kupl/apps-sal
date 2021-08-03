import sys


def input():
    return sys.stdin.readline().strip()


def main():
    N, K = list(map(int, input().split()))
    A = list(map(int, input().split()))
    B = K
    k = 1
    while K > 1:
        K //= 2
        k += 1
    if K == 0:
        print((sum(A)))
        return
    cnt = [0 for _ in range(k)]
    for a in A:
        for i in range(k):
            if (a >> i) & 1:
                cnt[i] += 1
    X = 0
    if N % 2 == 0:
        n = N // 2 - 1
    else:
        n = N // 2
    for i in range(k):
        if cnt[k - i - 1] <= n:
            if X + (2 ** (k - i - 1)) <= B:
                X += 2 ** (k - i - 1)
    answer = 0
    for a in A:
        answer += X ^ a
    print(answer)


def __starting_point():
    main()


__starting_point()
