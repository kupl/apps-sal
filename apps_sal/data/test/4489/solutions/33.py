from collections import defaultdict
cnt = defaultdict(int)
cnt[0] = 0
N = int(input())
for _ in range(N):
    cnt[input()] += 1
M = int(input())
for _ in range(M):
    cnt[input()] -= 1
print(max((v for v in list(cnt.values()))))
