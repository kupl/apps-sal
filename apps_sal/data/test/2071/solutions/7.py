import sys


def main():
    n = int(input().strip())
    a = list(map(int, input().strip().split()))
    b = list(map(int, input().strip().split()))

    d_a = [0 for _ in range(len(a))]
    d_b = [0 for _ in range(len(b))]

    sum = []
    for aa, bb in zip(reversed(a), reversed(b)):
        if len(sum) > 0:
            sum.append(aa + bb + sum[-1])
        else:
            sum.append(aa + bb)
    sum = list(reversed(sum))

    # print(sum)

    d_a[-1] = b[-1]
    d_b[-1] = a[-1]

    for i in reversed(list(range(n - 1))):
        # print(n-i)
        # print((n - i) * 2 - 1)
        d_a[i] = sum[i + 1] + d_a[i + 1] + ((n - i) * 2 - 1) * b[i]
        d_b[i] = sum[i + 1] + d_b[i + 1] + ((n - i) * 2 - 1) * a[i]

    ans = 0
    cur = 0

    for i in range(n):
        if i % 2 == 0:
            ans = max(
                cur + d_a[i] + sum[i] * 2 * i,
                ans
            )
            cur += 2 * i * a[i] + (2 * i + 1) * b[i]
            if i + 1 < n:
                ans = max(
                    cur + d_b[i + 1] + sum[i + 1] * (2 * i + 2),
                    ans
                )

        else:
            ans = max(
                cur + d_b[i] + sum[i] * 2 * i,
                ans
            )
            cur += 2 * i * b[i] + (2 * i + 1) * a[i]
            if i + 1 < n:
                ans = max(
                    cur + d_a[i + 1] + sum[i + 1] * (2 * i + 2),
                    ans
                )

    print(ans)

    return 0


def test(i):
    with open("test_{}.txt".format(i)) as fin:
        sys.stdin = fin
        main()


def __starting_point():
    # test(1)
    # test(2)
    return(main())

__starting_point()
