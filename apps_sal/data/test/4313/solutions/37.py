n = int(input())
v = [int(i) for i in input().split()]
c = [int(i) for i in input().split()]
res = 0
for i in range(n):
    if v[i] > c[i]:
        res += v[i] - c[i]
print(res)
