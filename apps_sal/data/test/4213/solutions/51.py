N = int(input())
A = list(map(int, input().split()))
diffmax = 0
for i in range(N):
    for j in range(1, N):
        diff = abs(A[i] - A[j])
        if diff > diffmax:
            diffmax = diff
print(diffmax)
