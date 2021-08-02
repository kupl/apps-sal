from bisect import bisect


def ctoi(c):
    return ord(c) - ord('a')


def solve():
    S = input()
    T = input()
    N = len(S)
    idx = [[] for i in range(26)]
    for i in range(2 * N):
        idx[ctoi(S[i % N])].append(i)
    ans = -1
    for c in T:
        if not idx[ctoi(c)]:
            return -1
        ans += idx[ctoi(c)][bisect(idx[ctoi(c)], ans % N)] - ans % N
    return ans + 1


print((solve()))
