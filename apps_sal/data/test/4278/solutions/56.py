import math
N = int(input())
S = [list(map(str, input())) for _ in range(N)]
S.sort()
for s in S:
    s.sort()

ans = 0

dic = {}

SS = []

for s in S:
    SS.append("".join(s))

for i in range(N):
    if SS[i] in dic:
        dic[SS[i]] += 1
    else:
        dic[SS[i]] = 1

for key in dic:
    if dic[key] > 1:
        ans += dic[key] * (dic[key] - 1) // 2

print(ans)
