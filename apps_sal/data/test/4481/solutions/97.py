N = int(input())
S = [input() for _ in range(N)]
S.sort()

res = 0
cnt = 1
for i in range(N-1):
    if S[i] == S[i+1]:
        cnt+=1
    else:
        res = max(res,cnt)
        cnt = 1

res = max(res,cnt)

cnt = 1
ans = []
for i in range(N-1):
    if S[i] == S[i+1]:
        cnt+=1
    else:
        if res == cnt:
            ans.append(S[i])
        cnt = 1

if cnt == res:
    ans.append(S[i+1])

for i in range(len(ans)):
    print((ans[i]))

