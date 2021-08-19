import sys
input = sys.stdin.readline
(N, K, Q) = map(int, input().split())
A = list(map(int, input().split()))
ans = float('inf')
for lb in sorted(A):
    tmp = []
    use = []
    for a in A + [-1]:
        if a >= lb:
            tmp.append(a)
        else:
            if len(tmp) >= K:
                use += sorted(tmp)[:len(tmp) - K + 1]
            tmp = []
    if len(use) < Q:
        break
    ans = min(ans, sorted(use)[Q - 1] - lb)
print(ans)
