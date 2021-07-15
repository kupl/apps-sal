N = int(input())
V = list(map(int, input().split()))

V.sort()

res = V[0]

for i in range(1, N):
    res += V[i] * 2**(i - 1)

print(res / 2**(N - 1))
