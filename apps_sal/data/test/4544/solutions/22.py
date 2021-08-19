from collections import defaultdict
n = int(input())
arr = list(map(int, input().split()))
d = defaultdict(int)
for x in arr:
    d[x] += 1
a = d[0] + d[1] + d[2]
ans = [a]
for i in range(max(arr) - 2):
    a -= d[i]
    a += d[i + 3]
    ans.append(a)
print(max(ans))
