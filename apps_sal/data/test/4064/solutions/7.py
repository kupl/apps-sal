import sys
input = sys.stdin.readline

n, h, l, r = list(map(int, input().split()))
A = list(map(int, input().split()))

DP = [-1] * h
DP[0] = 0

for a in A:
    NDP = [-1] * h
    for k in range(h):
        if DP[k] == -1:
            continue
        if l <= (a + k) % h <= r:
            NDP[(a + k) % h] = max(NDP[(a + k) % h], DP[k] + 1)
        else:
            NDP[(a + k) % h] = max(NDP[(a + k) % h], DP[k])

        if l <= (a + k - 1) % h <= r:
            NDP[(a + k - 1) % h] = max(NDP[(a + k - 1) % h], DP[k] + 1)
        else:
            NDP[(a + k - 1) % h] = max(NDP[(a + k - 1) % h], DP[k])

    DP = NDP

print(max(DP))
