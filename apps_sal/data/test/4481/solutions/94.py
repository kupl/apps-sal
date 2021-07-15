import collections
n = int(input())
ans = list(input() for i in range(n))
ans = collections.Counter(ans)
m = max(ans.values())
keys = [k for k, v in ans.items() if v == m]
[print(j) for j in sorted(keys)]
