(N, K) = map(int, input().split())
A = list(map(int, input().split()))
dic = {}
for a in A:
    if a in dic.keys():
        dic[a] += 1
    else:
        dic[a] = 1
dic = sorted(dic.items(), key=lambda x: x[1], reverse=True)
ans = 0
for (i, j) in dic[K:]:
    ans += j
print(ans)
