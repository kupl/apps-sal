N = int(input())
v = [int(c) for c in input().split()]

v.sort()
tmp = 0.0
for i in range(N):
    if i == 0:
        tmp = v[i]
    else:
        tmp = (tmp+v[i])/2.0

print(tmp)
