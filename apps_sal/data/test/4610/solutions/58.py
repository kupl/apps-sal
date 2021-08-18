N, K = map(int, input().split())
A = list(map(int, input().split()))


dic = {}
for i in range(N):
    a = A[i]
    if a not in dic:
        dic[a] = 1
    else:
        dic[a] += 1

dic = sorted(dic.items(), key=lambda x: x[1])

ans = 0
for i in range(max(len(dic) - K, 0)):
    ans += dic[i][1]

print(ans)
