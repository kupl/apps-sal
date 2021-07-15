n = int(input())
l = [*map(int, input().split())]

p = [0] * n
for i in range(n): p[l[i] - 1] = i

res = ['?'] * n

for e in range(n, 0, -1):
    i = p[e - 1]
    res[i] = 'B'
    for j in range(i % e, n, e):
        if i != j and l[i] <= l[j] and res[j] == 'B':
            res[i] = 'A'
            break 
print(''.join(res))
