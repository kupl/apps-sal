n, k = [int(i) for i in input().split()]
a = [int(i) for i in input().split()]
b = [i for i in a]
a.sort()
d = {}
count = 0
ans = []
ans_sum = 0
for i in range(n):
    if not b[i] in d:
        d[b[i]] = []
    d[b[i]].append(i)

for i in reversed(range(n)):
    ans_sum += a[i]
    ans.append(d[a[i]][0])
    d[a[i]] = d[a[i]][1:]
    count += 1
    if count == k:
        break

print(ans_sum)
ans.sort()
ans = [-1] + ans
l = len(ans)
for i in range(1, l - 1):
    print(ans[i] - ans[i - 1], end = " ")
print(n - ans[-2] - 1)
