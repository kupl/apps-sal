import sys
input = lambda: sys.stdin.readline().rstrip()

def chk(a):
    Y = [0] * (N + 10)
    for l, r, d in X:
        if d <= a: continue
        Y[l-1] += 1
        Y[r] -= 1
    for i in range(1, N+10):
        Y[i] += Y[i-1]
    return 1 if sum([min(Y[i], 1) for i in range(N+5)]) * 2 + N+1 <= T else 0

M, N, K, T = list(map(int, input().split()))
A = [int(a) for a in input().split()]
X = []
for _ in range(K):
    l, r, d = list(map(int, input().split()))
    X.append((l, r, d))

l, r = 0, 2*10**5
while r - l > 1:
    m = (l+r) // 2
    if chk(m):
        r = m
    else:
        l = m

print(len([a for a in A if a >= r]))


