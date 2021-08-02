def main():
    import sys
    input = sys.stdin.readline
    n, k = map(int, input().split())
    A = list(map(int, input().split()))
    A.sort()
    A.append(0)
    l1 = [0] * n
    for i in range(1, n):
        l1[i] = l1[i - 1] + (A[i] - A[i - 1]) * i
    l2 = [0] * n
    for i in range(1, n):
        l2[n - i - 1] = l2[n - i] + (A[n - i] - A[n - i - 1]) * i
    ans = float("INF")
    c = 1
    for i in range(n):
        if A[i + 1] == A[i]:
            c += 1
        else:
            c1 = i - c + 1
            c2 = n - i - 1
            if c >= k:
                ans = 0
            elif c + c1 >= k or c + c2 >= k:
                if c + c1 >= k:
                    ans = min(ans, l1[i] - c - c1 + k)
                if c + c2 >= k:
                    ans = min(ans, l2[i] - c - c2 + k)
            else:
                ans = min(ans, l1[i] + l2[i] - n + k)
            c = 1
    print(ans)


def __starting_point():
    main()


__starting_point()
