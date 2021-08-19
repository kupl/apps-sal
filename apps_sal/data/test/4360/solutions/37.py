N = int(input())
A = list(map(int, input().split()))
rev = 0
for i in range(N):
    rev += 1 / A[i]
print(1 / rev)
