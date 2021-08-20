from collections import defaultdict
charnums = defaultdict(int)
N = int(input())
for _ in range(N):
    charnums[input()] += 1
ans = []
m = max(charnums.values())
for (key, value) in charnums.items():
    if value == m:
        ans.append(key)
for an in sorted(ans):
    print(an)
