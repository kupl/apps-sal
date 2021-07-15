N = int(input())
A = list(map(int, input().split()))

x2 = 0
for i in range(N):
    if i % 2:
        x2 -= A[i]
    else:
        x2 += A[i]

ans = [0]*N
ans[0] = x2//2
for i in range(N-1):
    ans[i+1] = A[i]-ans[i]

for i in range(N):
    ans[i] *= 2

print((' '.join(map(str, ans))))

