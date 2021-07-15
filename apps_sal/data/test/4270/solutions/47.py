n = int(input())
v = list(map(int,input().split()))
v.sort()
v0 = v[0]
for i in range(1,n):
    v0 = (v0 + v[i]) / 2
print(v0)
