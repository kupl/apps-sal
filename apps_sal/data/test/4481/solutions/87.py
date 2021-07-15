from collections import Counter

N = int(input())
S = [input() for _ in range(N)]

cnts = Counter(S)
max_l = max(cnts.values())

ans = [s for s, c in cnts.items() if c == max_l]
ans.sort()

print(*ans, sep='\n')
