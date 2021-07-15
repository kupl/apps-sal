N = int(input())
t = [int(Ti) for Ti in input().split()]
v = [int(Vi) for Vi in input().split()]

v_max = [0]
for ti, vi in zip(t, v):
    v_max[-1] = min(v_max[-1], vi)
    for _ in range(2*ti):
        v_max.append(vi)

for i in range(len(v_max)-1):
    v_max[i+1] = min(v_max[i] + 0.5, v_max[i+1])

v_max[-1] = 0
for i in range(len(v_max)-2, -1, -1):
    v_max[i] = min(v_max[i], v_max[i+1] + 0.5)

area = 0
for i in range(len(v_max) - 1):
    area += 0.5 * 0.5 * (v_max[i] + v_max[i+1])

print(area)

