import sys
input = sys.stdin.readline

N, K, Q = map(int, input().split())
A = list(map(int, input().split()))
cannot_use = set([-1])
ans = float('inf')
for i in sorted(A):
    tmp = []
    use = []
    for a in A + [-1]:
        if a not in cannot_use:
            tmp.append(a)
        else:
            if len(tmp) >= K:
                tmp.sort()
                use += tmp[:len(tmp) - K + 1]
            tmp = []
    use.sort()
    if len(use) < Q:
        break
    ans = min(ans, use[Q - 1] - i)
    cannot_use.add(i)
print(ans)
