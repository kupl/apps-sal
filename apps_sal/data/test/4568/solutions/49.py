N = int(input())
S = list(input())
dic = {}

for i in range(N):
    if S[i] not in dic.keys():
        dic[S[i]] = [i]
    else:
        dic[S[i]].append(i)

ans = 0
for j in range(1, N):
    cnt = 0
    for k in dic.values():
        check1 = False
        check2 = False
        for l in k:
            if l < j:
                check1 = True
            if j <= l:
                check2 = True
        if check1 and check2:
            cnt += 1
    ans = max(ans, cnt)

print(ans)
