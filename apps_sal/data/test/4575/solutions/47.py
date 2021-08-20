N = int(input())
(D, X) = map(int, input().split())
A = [int(input()) for i in range(N)]
count = 0
for i in range(N):
    for j in range(100):
        if A[i] * j + 1 <= D:
            count += 1
print(count + X)
