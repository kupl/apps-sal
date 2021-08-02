K, N = list(map(int, input().split()))
dis = list(map(int, input().split()))
dif = []
for i in range(N - 1):
    dif.append(int(dis[i + 1] - dis[i]))

dif.append(int(K - dis[N - 1] + dis[0]))
print((K - max(dif)))
