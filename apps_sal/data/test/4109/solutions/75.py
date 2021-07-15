import sys
def input(): return sys.stdin.readline().rstrip()
INF = 10000000000000
N,M,X = map(int,input().split())

C = []
A = []
for i in range(N):
    vec = list(map(int,input().split()))
    C.append(vec[0])
    A.append(vec[1:])

ans = INF

for bit in range(1 << N):
    sum = 0
    skill = [0] * M
    for n in range(N):
        if bit & (1 << n):
            for i, s in enumerate(A[n],0):
                skill[i] += s
            sum += C[n]

    flag = True
    for i in range(M):
        if skill[i] < X:
            flag = False
            break
    if flag:
        ans = min(ans,sum)

if ans == INF:
    print(-1)
else:
    print(ans)
