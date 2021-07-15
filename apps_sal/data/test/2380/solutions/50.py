N, M = map(int, input().split())
A = list(map(int, input().split()))
D = {}
for a in A:
    if a in D:
        D[a] += 1
    else:
        D[a] = 1

for i in range(M):
    B, C = map(int, input().split())
    if C in D:
        D[C] += B
    else:
        D[C] = B

K = sorted(D.keys(), reverse=True)
ans = 0
cnt = N
for k in K:
   a = min(D[k], cnt)
   ans += k * a
   cnt -= a
   if cnt == 0: break
print(ans)
