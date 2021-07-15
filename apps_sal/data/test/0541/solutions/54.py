INF = 10**9

N, M = map(int, input().split())

requests =[]
for _ in range(M):
    requests.append(tuple(map(int, input().split())))
requests.sort(key=lambda x:x[1])

end = 1
ans = 0
for i in range(M):
    if end <= requests[i][0]:
        ans += 1
        end = requests[i][1]

print(ans)
