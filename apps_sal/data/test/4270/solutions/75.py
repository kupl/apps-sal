n = int(input())
v = list(map(int, input().split()))
v.sort()
t = float(v[0] + v[1]) / 2
for i in range(2, n, 1):
    t = float(t + v[i]) / 2
print('{:.05f}'.format(t))
