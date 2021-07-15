def main():
    n, m = list(map(int, input().split()))
    aa = sorted(map(int, input().split()))
    bb = [0] * (n + 1)
    for _ in range(m):
        l, r = list(map(int, input().split()))
        bb[l - 1] += 1
        bb[r] -= 1
    a = 0
    for i, b in enumerate(bb):
        a += b
        bb[i] = a
    del bb[-1]
    bb.sort()
    print(sum(a * b for a, b in zip(aa, bb)))


def __starting_point():
    main()

__starting_point()
