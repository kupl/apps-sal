n, M = list(map(int, input().split()))
A = [0] + list(map(int, input().split())) + [M]

total_on = 0
for i, a in enumerate(A):
    if i%2:
        total_on += a - A[i-1]

on = [[M-total_on]*(n+2), [total_on]*(n+2)]

for i in range(1, n+2):
    sw = i%2
    on[sw][i] = on[sw][i-1]-(A[i]-A[i-1])
    on[1-sw][i] = on[1-sw][i-1]

maxon = total_on
for i in range(n+1):
    if A[i] < A[i + 1] - 1:
        maxon = max(maxon, total_on + on[0][i+1-i%2] - on[1][i+1] - 1)

print(maxon)


