x = int(input())
y = list(map(int, input().split(' ')))
y.sort()
c = y[0]
add = 0
for i in range(1, x):
    if y[i] > c:
        c = y[i]
    else:
        c = c + 1
        add += c - y[i]
print(add)
