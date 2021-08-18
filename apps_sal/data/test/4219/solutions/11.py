def main():
    import numpy as np

    N = int(input())
    testimony = np.zeros((N, N), dtype=np.int64)
    for i in range(N):
        A = int(input())
        INF = 10 ** 10
        for _ in range(A):
            x, y = list(map(int, input().split()))
            testimony[i, x - 1] += 1 if y else -INF

    ans = 0
    for bit in range(1 << N):
        honest = set()
        pick = np.zeros(N, dtype=np.int64)
        for i in range(N):
            if bit & (1 << i):
                honest.add(i)
                pick += testimony[i, :]
        flag = True
        for j in range(N):
            value = pick[j]
            if (0
                    or (j in honest and value < 0)
                    or (j not in honest and value > 0)
                    or (value < 0 and value % INF != 0)):
                flag = False
                break
        if flag:
            ans = max(ans, len(honest))
    print(ans)


def __starting_point():
    main()


__starting_point()
