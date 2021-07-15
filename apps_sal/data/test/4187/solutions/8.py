import itertools

n = int(input())
a = list(map(int, input().split()))

i = a.index(0)
a = a[i:]+a[:i]

result = max(len(list(g))*k for k, g in itertools.groupby(a))

print(result)
