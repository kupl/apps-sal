def resolve():
    """
    code here
    """
    N = int(input())
    starts = [[int(item) for item in input().split()] for _ in range(N - 1)]
    for i in range(N):
        temp_time = 0
        if i == N - 1:
            print(0)
        else:
            for j in range(i, N - 1):
                (c, s, f) = starts[j]
                if temp_time <= s:
                    temp_time = s
                if temp_time % f == 0:
                    pass
                else:
                    temp_time = (temp_time // f + 1) * f
                temp_time += c
            print(temp_time)


def __starting_point():
    resolve()


__starting_point()
