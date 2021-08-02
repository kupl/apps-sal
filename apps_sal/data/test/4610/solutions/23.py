N, K = list(map(int, input().split()))
A = list(map(int, input().split()))

dic = {}
for i in A:
    if i not in list(dic.keys()):
        dic[i] = 1
    else:
        dic[i] += 1
dic = sorted(list(dic.items()), key=lambda x: x[1], reverse=True)
k = 0
ans = 0
for key, value in dic:
    if k >= K:
        ans += value
    k += 1
print(ans)
