n = int(input())
v = list(map(int, input().split()))
for i in range(n - 1):
    v.sort()
    v.append((v[0] + v[1]) / 2)
    v.pop(0)
    v.pop(0)
print(v[0])
