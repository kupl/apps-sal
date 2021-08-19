(n, m, k) = map(int, input().split())
x = 1
y = 1
a = [[1, 1]]
inv = 1
z = n * m
while z > 1:
    z -= 1
    if y < m and inv == 1:
        y += 1
    elif y > 1 and inv == -1:
        y -= 1
    else:
        x += 1
        inv = -inv
    a.append([x, y])
while k > 1:
    print(2, *a.pop(), end=' ')
    print(*a.pop())
    k -= 1
print(len(a), end=' ')
for i in a:
    print(*i, end=' ')
print()
