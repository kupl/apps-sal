N = int(input())
S = [input() for _ in range(N)]
cnts = {key: 0 for key in S}
for key in S:
    cnts[key] += 1
max_cnt = max(cnts.values())
ans = [k for (k, v) in cnts.items() if v == max_cnt]
ans.sort()
print(*ans, sep='\n')
