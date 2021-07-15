N,A,B = map(int,input().split())
if A+B > N+1 or A*B < N:
    print(-1)
    return

ls = [1]*B
rem = N-B
i = 0
while rem > 0:
    r = min(A-1, rem)
    ls[i] += r
    rem -= r
    i += 1

bs = [[] for _ in range(B)]
n = 1
for j,l in enumerate(ls):
    for i in range(l):
        bs[j].append(n)
        n += 1
ans = []
for b in reversed(bs):
    ans += b
print(*ans)
