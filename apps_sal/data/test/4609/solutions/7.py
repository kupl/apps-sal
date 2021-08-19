N = int(input())
A = [0] * N
for i in range(N):
    A[i] = int(input())
A.sort()
count = 1
ans = 0
for i in range(N - 1):
    if A[i] == A[i + 1]:
        count += 1
    else:
        ans += count % 2
        count = 1
ans += count % 2
print(ans)
