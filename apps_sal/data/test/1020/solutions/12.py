(x, y, k) = (int(e) for e in input().split(' '))
r = 0
for i in range(k):
    r += 2 * (x + y - 2)
    x -= 4
    y -= 4
print(r)
' \n3 3 1\n8\n'
