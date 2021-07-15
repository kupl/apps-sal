from collections import Counter
n = int(input())
arr = list(map(int, input().split()))
max_i = -1
max_n = -1
ans = Counter()
for x in arr:
    ans[x] += 1
    if ans[x] > max_n:
        max_i = x
        max_n = ans[x]
print(max_i)

