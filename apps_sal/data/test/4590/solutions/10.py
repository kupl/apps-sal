def main():
    n, m, k = list(map(int, input().split()))
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))

    s = sum(B)
    ans = 0
    i, j = 0, m - 1
    while i < n:
        if s <= k:
            ans = max(ans, i + j + 1)
            s += A[i]
            i += 1
        else:
            if j < 0:
                break
            s -= B[j]
            j -= 1

    if s <= k:
        ans = max(ans, n + j + 1)

    print(ans)
    return


def __starting_point():
    main()

__starting_point()
