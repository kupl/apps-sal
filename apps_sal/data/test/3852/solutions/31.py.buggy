#!python3

# input
N = int(input())
A = list(map(int, input().split()))


def main():
    mx = max(A)
    mn = min(A)
    idx = A.index(mn) if abs(mx) < abs(mn) else A.index(mx)
    idx += 1
    ans = []
    for i in range(N):
        ans.append((idx, i + 1))

    if A[idx - 1] > 0:
        for i in range(1, N):
            ans.append((i, i + 1))
    else:
        for i in range(N - 1, 0, -1):
            ans.append((i + 1, i))

    n = len(ans)
    print(n)
    for i in range(n):
        print((*ans[i]))


def __starting_point():
    main()


__starting_point()
