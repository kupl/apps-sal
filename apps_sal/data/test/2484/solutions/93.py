def abc098_d():
    n = int(input())
    A = list(map(int, input().split()))
    ans = 0
    rt = 0
    total = 0
    for lf in range(n):
        while rt < n:
            if total ^ A[rt] == total + A[rt]:
                total += A[rt]
                rt += 1
            else:
                break
        ans += rt - lf
        if lf == rt:
            rt += 1
        else:
            total -= A[lf]
    print(ans)


def __starting_point():
    abc098_d()


__starting_point()
