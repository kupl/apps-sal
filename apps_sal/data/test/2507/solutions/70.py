import numpy as np

def main():
    N, K = list(map(int, input().split()))
    A = np.array(list(map(int, input().split())))
    F = np.array(list(map(int, input().split())))

    A.sort()
    F = np.sort(F)[::-1]

    time = A*F
    high = 10**12 + 1
    low = -1

    while high - low > 1:
        middle = (high + low) // 2

        temp = np.where(time>middle, time-middle, 0)
        temp = np.ceil(temp/F).sum()

        if temp <= K:
            high = middle
        else:
            low = middle

    middle = high
    temp = np.where(time>middle, time-middle, 0)
    temp = np.ceil(temp/F)
    time = (time - temp*F).max()
    print((int(time)))


def __starting_point():
    main()

__starting_point()
