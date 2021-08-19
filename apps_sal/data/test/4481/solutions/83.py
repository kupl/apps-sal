N = int(input())
(dic, lis) = ({}, [])
for i in range(N):
    s = input()
    if s in dic:
        dic[s] += 1
    else:
        dic[s] = 1
M = max(dic.values())
for s in dic.keys():
    if dic[s] == M:
        lis.append(s)
ans = sorted(lis)
for s in ans:
    print(s)
