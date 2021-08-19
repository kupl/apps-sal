N = int(input())
T = list(map(int, input().split()))
sum = 0
for _ in range(N):
    sum += T[_]
M = int(input())
for i in range(M):
    (a, b) = list(map(int, input().split()))
    print(sum + b - T[a - 1])
