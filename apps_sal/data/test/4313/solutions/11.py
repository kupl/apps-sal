N = int(input())
V = [int(x) for x in input().split()]
C = [int(x) for x in input().split()]

result = 0
for i in range(N):
    result += max(0, V[i] - C[i])
print(result)
