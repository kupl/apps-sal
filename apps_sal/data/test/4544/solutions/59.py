import collections

N = int(input())
a = list(map(int, input().split()))

for i in range(len(a)):
    if a[i] > 0:
        a.append(a[i] - 1)
    a.append(a[i] + 1)

res = collections.Counter(a)

print(max(res.values()))
