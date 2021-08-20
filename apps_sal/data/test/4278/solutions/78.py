from collections import defaultdict, Counter
N = int(input())
S = [str(input()) for _ in range(N)]
D = defaultdict(int)
for s in S:
    cur = sorted(s)
    cur = ''.join(map(str, cur))
    D[cur] += 1
cnt = 0
for c in D.values():
    cnt += c * (c - 1) // 2
ans = cnt
print(ans)
