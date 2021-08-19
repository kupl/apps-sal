from collections import Counter
ans = Counter()
input()
for (i, b) in enumerate(map(int, input().split())):
    ans[b - i] += b
print(max(ans.values()))
