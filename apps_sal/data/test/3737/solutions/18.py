n = int(input())
a = [int(x) for x in input().split(' ')]
m = min(a)
M = max(a)
res = n
res -= len([x for x in a if x == m or x == M])
print(res)
