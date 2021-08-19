N = int(input())
output = [0] * N
for i in range(N - 1):
    (u, v) = [int(v) for v in input().split(' ')]
    output[u - 1] += 1
    output[v - 1] += 1
print(output.count(1))
