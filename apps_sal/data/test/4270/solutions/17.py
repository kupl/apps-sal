N = int(input())
v = sorted([int(i) for i in input().split()])
for i in range(N - 1):
    a = v.pop(0)
    b = v.pop(0)
    v.append((a + b) / 2)
    v.sort()
print(v[0])
