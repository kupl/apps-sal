def main():
    n, k = list(map(int, input().split()))
    V = list(map(int, input().split()))
    ans = -1
    for i in range(c := min(n, k) + 1):
        for j in range(c - i):
            A = V[:i] + V[-j:] if j != 0 else V[:i]
            A.sort(reverse=True)
            r = k - (i + j)
            for _ in range(r):
                if len(A) == 0:
                    break
                if (a := A.pop()) >= 0:
                    A.append(a)
                    break
            ans = max(ans, sum(A))
    print(ans)


def __starting_point():
    main()


__starting_point()
