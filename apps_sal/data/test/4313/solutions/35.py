n = int(input())
v = [int(x) for x in input().split()]
c = [int(x) for x in input().split()]
l = [0] * n

for i in range(n):
    l[i] = v[i] - c[i]
    if(l[i] < 0):
        l[i] = 0

print(sum(l))
