n = int(input())
v = list(map(int, input().split()))
v.sort()
z = (v[0] + v[1]) / 2
for i in range(2, n):
    z = (z + v[i]) / 2

print(z)
