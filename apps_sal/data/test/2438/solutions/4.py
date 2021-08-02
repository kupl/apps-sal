import sys
readline = sys.stdin.readline
N = int(readline())
S = [1 if s == 'A' else 0 for s in readline().strip()]
ans = 0
L1 = [None] * (N + 1)
L2 = [None] * (N + 1)
for i in range(N - 1, -1, -1):
    s = S[i]
    L1[i] = L1[i + 1]
    L2[i] = L2[i + 1]
    if s == 1:
        L1[i] = i
    else:
        L2[i] = i

for i in range(N - 1):
    s = S[i]
    sn = S[i + 1]
    if s == sn:
        if s == 1:
            if L2[i] is not None:
                ans -= 1
        else:
            if L1[i] is not None:
                ans -= 1
    else:
        if s == 1:
            if L1[i + 1] is None:
                ans -= N - i - 1
            else:
                ans -= L1[i + 1] - (i + 1)
        else:
            if L2[i + 1] is None:
                ans -= N - i - 1
            else:
                ans -= L2[i + 1] - (i + 1)
print((N - 1) * N // 2 + ans)
