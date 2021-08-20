(n, m) = map(int, input().split())
city = [0] * n
for i in range(m):
    (a, b) = map(int, input().split())
    city[a - 1] += 1
    city[b - 1] += 1
for i in city:
    print(i)
