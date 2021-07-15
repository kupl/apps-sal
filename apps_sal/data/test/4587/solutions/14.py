def binary_search(lst, t, i):
    left = -1
    right = len(lst)

    while abs(right - left) > 1:
        mid = (left + right) // 2
        if i == 0:
            if lst[mid] < t:
                left = mid
            else:
                right = mid
        elif i == 1:
            if lst[mid] > t:
                right = mid
            else:
                left = mid

    return left


def main():
    n = int(input())
    A = sorted(list(map(int, input().split())))
    B = sorted(list(map(int, input().split())))
    C = sorted(list(map(int, input().split())))
    ans = 0

    for b in B:
        a = binary_search(A, b, 0)
        c = binary_search(C, b, 1)
        ans += (a + 1) * (n - c - 1)

    print(ans)


def __starting_point():
    main()

__starting_point()
