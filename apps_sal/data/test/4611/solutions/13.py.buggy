n = int(input())
t = 0
x = 0
y = 0
for i in range(n):
    t_, x_, y_ = map(int, input().split())
    t = abs(t_ - t)
    x = abs(x_ - x)
    y = abs(y_ - y)
    if x + y > t:
        print('No')
        return
    if t_ % 2 != (x_ + y_) % 2:
        print('No')
        return

print('Yes')
