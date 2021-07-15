def main():
    N = int(input())
    A = reversed(list(map(int, input().split())))
    balls = [0] * (N + 1)
    for i, a in enumerate(A):
        s = sum([balls[j] for j in range((N-i)*2, N+1, (N-i))])
        if (a == 1 and s % 2 == 0) or (a == 0 and s % 2 == 1):
            balls[N-i] = 1
    print((sum(balls)))
    idx = [str(i) for i, flag in enumerate(balls) if flag == 1]
    print((' '.join(idx)))


def __starting_point():
    main()

__starting_point()
