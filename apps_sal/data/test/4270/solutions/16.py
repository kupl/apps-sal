N = int(input())
v = list(map(int, input().split()))
v.sort()
x = (v[0] + v[1]) / 2
for i in range(2, N):
    x = (x + v[i]) / 2
print(x)
