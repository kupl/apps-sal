n = int(input())
data = [list(map(int, input().split())) for _ in range(n)]
data.sort(key = lambda x: x[0]-x[1])
print(sum(v[1]*i + v[0]*(n-i-1) for i, v in enumerate(data)))
