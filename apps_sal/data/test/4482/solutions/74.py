N = int(input())
A = list(map(int, input().split()))
ans = 0
if sum(A) % N == 0:
    x = sum(A) // N
    for i in range(N):
        ans += (x - A[i]) ** 2
    print(ans)
else:
    x = sum(A) // N
    b = sum(A) // N + 1
    if sum(A) / N - x > b - sum(A) / N:
        x = b
    for i in range(N):
        ans += (x - A[i]) ** 2
    print(ans)
