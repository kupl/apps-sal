n = int(input())
A = list(map(int, input().split()))

total = 0

for i in range(n):
    total += 1 / A[i]

print(1 / total)
