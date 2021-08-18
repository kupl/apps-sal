n, a, x, b, y = list(map(int, input().split()))

while(a != x and b != y):
    a = (a) % n + 1
    b = (b - 2) % n + 1
    if(a == b):
        print('YES')
        return
    if(a == x or b == y):
        break
print('NO')
