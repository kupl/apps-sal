(n, v) = [int(i) for i in input().split()]
f = 0
l = [0] * 3002
for i in range(n):
    (a, b) = [int(i) for i in input().split()]
    l[a] += b
for i in range(1, 3002):
    pick = min(v, l[i - 1])
    l[i - 1] -= pick
    pick2 = min(v - pick, l[i])
    l[i] -= pick2
    f += pick + pick2
print(f)
