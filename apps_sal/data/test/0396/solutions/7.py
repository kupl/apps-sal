l, r = map(int, input().split())
a = 1
b = 1
ans = 0
while True:
    b = 1
    while True:
        if a * b > r:
            break
        if a * b >= l:
            ans += 1
        b = 3 * b
    a = 2 * a
    if(a > r):
        break
print(ans)
