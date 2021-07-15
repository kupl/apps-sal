


input()
A = list(map(int,input()))
f = tuple(map(int,input().split()))

for i,a in enumerate(A):
    if a < f[a-1]:
        break
for j,a in enumerate(A[i:], start=i):
    if a > f[a-1]:
        break
    else:
        A[j] = f[a-1]

print(*A, sep='')
