x = int(input())
y = list(map(float, input().split(' ')))
y.sort()
y.reverse()
l = [y[0]]
p = y[0]
prod = 1 - y[0]

for i in range(1, x):

    newx = p * (1 - y[i]) + prod * y[i]
    if newx > p:
        prod *= (1 - y[i])
        p = newx
        l.append(y[i])

print(p)
