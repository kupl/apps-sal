m = int(input())
d = {}
for i in range(m):
    a, v = map(int, input().split())
    d[a] = v
n = int(input())
for i in range(n):
    a, v = map(int, input().split())
    if(a in d):
        d[a] = max(d[a], v)
    else:
        d[a] = v
# print(d)
l = d.values()
print(sum(l))
