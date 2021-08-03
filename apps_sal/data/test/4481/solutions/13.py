N = int(input())
S = [input() for _ in range(N)]

dic = {}

for i in range(N):
    if S[i] not in list(dic.keys()):
        dic[S[i]] = 1

    else:
        dic[S[i]] += 1

maxim = max(dic.values())
ans = []

for keys in list(dic.keys()):
    if dic[keys] == maxim:
        ans.append(keys)

ans.sort()

for i in range(len(ans)):
    print((ans[i]))
