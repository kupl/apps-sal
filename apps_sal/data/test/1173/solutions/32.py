import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 7)
N = int(input())
A = [list([int(n) - 1 for n in input().split()]) for i in range(N)]
cur = [0 for i in range(N)]
que = [i for i in range(N)]
ans = 0
while len(que) > 0:
    done = set()
    que2 = []
    for n in que:
        if n in done:
            continue
        pair = A[n][cur[n]]
        if pair in done:
            continue
        if n == A[pair][cur[pair]]:
            cur[n] += 1
            cur[pair] += 1
            done.add(n)
            done.add(pair)
            if cur[n] < N - 1:
                que2.append(n)
            if cur[pair] < N - 1:
                que2.append(pair)
    if len(done) > 0:
        ans += 1
    que = que2
ok = True
for i in range(N):
    if cur[i] < N - 1:
        ok = False
if ok:
    print(ans)
else:
    print(-1)
