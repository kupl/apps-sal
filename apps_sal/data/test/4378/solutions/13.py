n = int(input())
g = list(input())
cost = 0

for i in range(1, n):
    if g[i] == g[i-1]:
        cost += 1
        if i == n - 1 or g[i] == g[i+1]:
            if g[i] == 'R': g[i] = 'G'
            elif g[i] == 'G': g[i] = 'B'
            else: g[i] = 'R'
        else:
            if g[i] == 'R' and g[i+1] == 'G':
                g[i] = 'B'
            elif g[i] == 'R' and g[i+1] == 'B':
                g[i] = 'G'
            elif g[i] == 'G' and g[i+1] == 'R':
                g[i] = 'B'
            elif g[i] == 'G' and g[i+1] == 'B':
                g[i] = 'R'
            elif g[i] == 'B' and g[i+1] == 'R':
                g[i] = 'G'
            else:
                g[i] = 'R'

print(cost)
print(''.join(g))

