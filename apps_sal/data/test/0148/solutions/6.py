n, a, x, b, y = list(map(int, input().split()))
while a != x and b != y:
    a += 1
    b -= 1
    if a == n + 1:
        a = 1
    if b == 0:
        b = n
    if a == b:
        print('YES')
        return
##    print(a, b)
print('NO')

