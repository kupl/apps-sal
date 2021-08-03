N, A, B = map(int, input().split())

if N < A + B - 1:
    print(-1)

else:
    if A > B:
        mode = 0
        A -= 1
    else:
        mode = 1
        B -= 1

    ret = []
    u = N - A + 1
    l = B
    while len(ret) < N:
        if (mode and A == 0) or (not mode and B == 0):
            ret = [-1]
            break

        if mode:
            for i in range(max(u, l - B + 1), u + A):
                ret.append(i)
            A -= 1
            u -= A
            mode ^= 1
        else:
            for i in range(min(l, u + A - 1), l - B, -1):
                ret.append(i)
            B -= 1
            l += B
            mode ^= 1

    print(*ret)
