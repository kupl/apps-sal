N, M = list(map(int, input().split()))
A = list(map(int, input().split()))
f = [-1, 2, 5, 5, 4, 5, 6, 3, 7, 6]

dp = [None] * (N + 1)
dp[0] = ""


def max_str(s1: str, s2: str) -> str:
    """return bigger one"""
    l1, l2 = len(s1), len(s2)
    if l1 != l2:
        return s1 if l1 > l2 else s2
    if l1 == l2:
        return s1 if s1 > s2 else s2


for i in range(2, N + 1):
    nxt = ""
    for aj in A:
        if i - f[aj] < 0 or dp[i - f[aj]] == None:
            continue
        nxt = max_str(nxt,
                      dp[i - f[aj]] + str(aj))
    if nxt != "":
        dp[i] = nxt
print((dp[N]))
