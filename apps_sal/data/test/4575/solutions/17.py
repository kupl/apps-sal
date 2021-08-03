N = int(input())
D, X = list(map(int, input().split()))
A = [0] * N
cnt = 0

for i in range(N):
    A[i] = int(input())
    j = 0
    while j * A[i] + 1 <= D:
        cnt += 1
        j += 1
ans = cnt + X

print(ans)
