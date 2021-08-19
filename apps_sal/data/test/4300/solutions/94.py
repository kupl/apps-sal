N = int(input())
d = [int(x) for x in input().split()]
result = 0
for i in range(N):
    for j in range(i + 1, N):
        result += d[i] * d[j]
print(result)
