n = int(input())
s = 0
a = 0
b = 0
for i in range(n):
    t, x, y = map(int, input().split())
    if t - s - abs(x - a) - abs(y - b) >= 0 and (t - s - abs(x - a) - abs(y - b)) % 2 == 0:
        s = t
        a = x
        b = y
    else:
        print('No')
        return
print('Yes')
