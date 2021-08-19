def __starting_point():
    (N, A, B) = map(int, input().split())
    S = (A + B) * 1000
    ans = 0
    if N > A + B:
        ans = A * (N // (A + B))
        if A > N % (A + B):
            ans += N % (A + B)
        else:
            ans += A
    elif N < A + B:
        if A > N:
            ans = N
        else:
            ans = A
    else:
        ans = A
    print(ans)


__starting_point()
