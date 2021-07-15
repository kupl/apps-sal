def solve(N, M, A):
    strs = set(A)
    used = set()
    forward = []
    mid = []

    for x in strs:
        rev = x[::-1]
        if x == rev:
            mid.append(x)
        elif rev in strs and x not in used:
            forward.append(x)
            used.add(x)
            used.add(rev)

    front = "".join(forward)
    back = front[::-1]
    if mid:
        ret = front + next(iter(mid)) + back
    else:
        ret = front + back
    return str(len(ret)) + "\n" + ret


def __starting_point():

    N, M = list(map(int, input().split()))
    A = []
    for i in range(N):
        S = input()
        assert len(S) == M
        A.append(S)
    ans = solve(N, M, A)
    print(ans)

__starting_point()
