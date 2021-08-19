import sys
readline = sys.stdin.readline
T = int(readline())
Ans = [None] * T
for qu in range(T):
    (N, M) = map(int, readline().split())
    A = list(map(int, readline().split()))
    B = list(map(int, readline().split()))
    A.reverse()
    res = 0
    seen = set()
    for b in B:
        res += 1
        if b in seen:
            seen.remove(b)
            continue
        res += 2 * len(seen)
        while A[-1] != b:
            seen.add(A.pop())
            res += 2
        A.pop()
    Ans[qu] = res
print('\n'.join(map(str, Ans)))
