import sys
readline = sys.stdin.readline

T = int(readline())
Ans = []
for qu in range(T):
    N, K = map(int, readline().split())
    A = list(map(int, readline().split()))
    SA = set(A)
    if len(SA) <= K:
        res = list(SA)
        for i in range(1, N + 1):
            if len(res) == K:
                break
            if i not in SA:
                res.append(i)
        Ans.append(str(N * K))
        Ans.append(' '.join(map(str, res * N)))
    else:
        Ans.append('-1')
print('\n'.join(map(str, Ans)))
