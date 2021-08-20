n = int(input())
v = [int(s) for s in input().split()]
v.sort()
avg = v[0]
for i in range(1, n):
    avg = avg / 2 + v[i] / 2
print(avg)
