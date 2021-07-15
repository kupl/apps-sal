N = int(input())
v = list(map(float, input().split()))

v.sort()

for i in range(N-1):
    v[i+1] = (v[i] + v[i+1]) / 2

print((v[-1]))

