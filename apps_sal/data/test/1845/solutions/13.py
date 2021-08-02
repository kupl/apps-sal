n = int(input())
l = list(map(int, input().split()))
cnt = sum(l)
ans = []
ans.append(cnt)
l = set(l)
l = list(l)
for i in range(len(l)):
    tmp = []
    for k in range(1, l[i] + 1):
        if l[i] % k == 0:
            tmp.append(k)
    for k in range(len(tmp)):
        for j in range(len(l)):
            if i == j:
                continue
            ans.append(cnt - l[i] - l[j] + l[i] // tmp[k] + l[j] * tmp[k])
ans.sort()
print(ans[0])
