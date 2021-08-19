def main():
    N = int(input())
    A = list(map(int, input().split()))
    ret = 0
    right = 0
    tot = 0
    for left in range(0, N):
        while right < N and (tot ^ A[right] == tot + A[right] or left == right):
            tot += A[right]
            right += 1
        ret += right - left
        tot = tot ^ A[left]
    print(ret)


def __starting_point():
    main()


__starting_point()
