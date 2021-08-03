from collections import Counter


def solve():
    ans = 0
    N = int(input())
    V = list(map(int, input().split()))
    V1 = [V[i] for i in range(0, N, 2)]
    V2 = [V[i] for i in range(1, N, 2)]
    v1 = Counter(V1)
    v2 = Counter(V2)
    v1 = sorted(v1.items(), key=lambda x: -x[1])
    v2 = sorted(v2.items(), key=lambda x: -x[1])
    if v1[0][0] != v2[0][0]:
        ans = N - (v1[0][1] + v2[0][1])
    else:
        if len(v1) == 1:
            if len(v2) == 1:
                return N // 2
            return N - (v1[0][1] + v2[1][1])
        if len(v2) == 1:
            return N - (v1[1][1] + v2[0][1])
        ans = N - max(v1[1][1] + v2[0][1], v1[0][1] + v2[1][1])
    return ans


print(solve())
