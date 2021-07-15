N = int(input())
S = [list(map(str, input())) for _ in range(N)]
S.sort()
for s in S:
    s.sort()

ans = 0
dic = {}

for s in S:
    ss = "".join(s)
    if ss in dic:
        ans += dic[ss]
        dic[ss] += 1
    else:
        dic[ss] = 1

print(ans)
