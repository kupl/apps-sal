N, M = map(int, input().split())
city = [0] * N

for _ in range(M):
    a, b = map(int, input().split())
    city[a - 1] += 1
    city[b - 1] += 1

for ans in city:
    print(ans)
