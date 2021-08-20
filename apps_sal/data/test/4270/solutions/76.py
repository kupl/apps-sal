n = int(input())
v = list(map(int, input().split()))
v.sort()
for i in range(1, n):
    v[i] = (v[i] + v[i - 1]) / 2
print(v[-1])
