def main():
    n = int(input())
    (A, B) = ([], [])
    for _ in range(n):
        (a, b) = list(map(int, input().split()))
        A.append(a)
        B.append(b)
    (A, B) = (sorted(A), sorted(B))
    if n % 2 == 0:
        (a_m, b_m) = (A[n // 2] + A[n // 2 - 1], B[n // 2] + B[n // 2 - 1])
        print(b_m - a_m + 1)
    else:
        (a_m, b_m) = (A[n // 2], B[n // 2])
        print(b_m - a_m + 1)


def __starting_point():
    main()


__starting_point()
