from collections import defaultdict as df
n = int(input())
d = df(list)
a = list(map(int, input().rstrip().split()))
for i in range(n):
    d[a[i]].append(i + 1)
a.sort(reverse=True)
a = list(set(a))
a.sort(reverse=True)
sum1 = 0
ans = []
counter = 0
for i in range(len(a)):
    for j in d[a[i]]:
        sum1 += (a[i] * counter) + 1
        counter += 1
        ans.append(j)
print(sum1)
print(*ans)
