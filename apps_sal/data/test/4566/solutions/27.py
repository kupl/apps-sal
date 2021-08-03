N, M = map(int, input().split())
city = [0] * N
for i in range(M):
    road = list(map(int, input().split()))
    for j in road:
        city[j - 1] += 1
for i in city:
    print(i)
