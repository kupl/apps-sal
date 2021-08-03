import sys
readline = sys.stdin.readline


N, K = list(map(int, readline().split()))
A = list(map(int, readline().split()))
C = [None] + list(map(int, readline().split()))
table = [0] * (K + 1)
for a in A:
    table[a] += 1
for i in range(K - 1, -1, -1):
    table[i] += table[i + 1]

ok = N
ng = 0
while abs(ok - ng) > 1:
    med = (ok + ng) // 2
    if all(-(-table[k] // med) <= C[k] for k in range(1, K + 1)):
        ok = med
    else:
        ng = med

A.sort(reverse=True)
Ans = [[] for _ in range(ok)]

for i in range(N):
    Ans[i % ok].append(A[i])

sys.stdout.write('{}\n'.format(ok))
for i in range(ok):
    sys.stdout.write('{} '.format(len(Ans[i])))
    sys.stdout.write('{}\n'.format(' '.join(map(str, Ans[i]))))
