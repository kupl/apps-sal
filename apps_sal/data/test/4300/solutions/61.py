import itertools
n = int(input())
l = list(map(int, input().split()))
c = itertools.combinations(l, 2)
ans = sum((x * y for (x, y) in c))
print(ans)
