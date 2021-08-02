N = int(input())
A = list(map(int, input().split()))

bunbo = 0

for i in range(N):
    bunbo += 1 / A[i]

print(1 / bunbo)
