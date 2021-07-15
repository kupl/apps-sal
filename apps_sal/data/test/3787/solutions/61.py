import sys
def MI(): return list(map(int,sys.stdin.readline().rstrip().split()))


N,A,B = MI()

if not (A+B <= N+1 and A*B >= N):
    print((-1))
    return

ANS = [[i for i in range(1,A+1)]]
if B >= 2:
    a = A+1
    q,r = divmod(N-A,B-1)
    for i in range(B-1-r):
        ANS.append([i for i in range(a,a+q)])
        a += q
    for i in range(r):
        ANS.append([i for i in range(a,a+q+1)])
        a += q+1

ANS.reverse()
ans = []
for X in ANS:
    for i in range(len(X)):
        ans.append(X[i])

print((*ans))

