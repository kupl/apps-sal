l = [int(x) for x in input().split()]
k = int(input())
m = max(l)
l.remove(max(l))
for i in range(k):
    m *= 2
print(sum(l) + m)
