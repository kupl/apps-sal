dp = dict()

n = int(input())
a = list(map(int, input().split()))
g = sorted(list(range(n)), key = lambda x: a[x])
value = a[g[0]] - 1
for i in g:
    if a[i] <= value:
        a[i] = value + 1
        value += 1
    else:
        value = a[i]
print(' '.join(map(str, a)))

