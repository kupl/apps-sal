N = int(input())
A = list(map(int, input().split()))
Sum = 0

for i in range(N):
    Sum += 1 / A[i]

print(1 / Sum)
