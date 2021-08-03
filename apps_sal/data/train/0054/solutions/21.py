Q = int(input())


def solve():
    N = int(input())
    S = list(map(int, input().split()))
    S = sorted(S)

    while len(S) > 1:
        if S[0] == 2048:
            return True

        if S[0] == S[1]:
            S = [2 * S[0]] + S[2:]
        else:
            S = S[1:]
        S = sorted(S)

    return 2048 in S


for _ in range(Q):
    if solve():
        print("YES")
    else:
        print("NO")
