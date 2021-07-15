import sys
input = sys.stdin.readline

N = int(input())
A = [list([int(n)-1 for n in input().split()]) for i in range(N)]
cur = [0 for i in range(N)]
que = [i for i in range(N)]
ans = 0
while len(que) > 0:
    done = {}
    que2 = []
    for n in que:
        if done.get(n):
            continue
        pair = A[n][cur[n]]
        if done.get(pair):
            continue
        if n == A[pair][cur[pair]]:
            cur[n] += 1
            cur[pair] += 1
            done[n] = True
            done[pair] = True
            if cur[n] < N-1:
                que2.append(n)
            if cur[pair] < N-1:
                que2.append(pair)
    if len(done) > 0:
        ans += 1
    que = que2
ok = True
for i in range(N):
    if cur[i] < N-1:
        ok = False
if ok:
    print(ans)
else:
    print((-1))

