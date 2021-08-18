

def main():
    import numpy as np

    N, M = list(map(int, input().split()))
    ab = np.array([list(map(int, input().split())) for _ in range(M)])
    for i in range(1, N + 1):
        print((np.count_nonzero(ab == i)))


main()
