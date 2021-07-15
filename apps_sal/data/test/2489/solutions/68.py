N = int(input())
A = sorted(list(map(int,input().split())))
lim = max(A)
B = [0] * (lim+1)
for i in range(N):
    B[A[i]] += 1
ans = N
for i in range(1,lim+1):
    if B[i] == 0:
        continue
    if B[i] >= 2:
        ans -= B[i]
        B[i] = 0
    for j in range(i*2,lim+1,i):
        ans -= B[j]
        B[j] = 0

print(ans)

