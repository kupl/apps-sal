x = int(input())
t = [1, 0, 0, 0, 1, 0, 1, 0, 2, 1, 1, 2, 0, 1, 0, 0]
if x == 0:
    print('1')
    return
y = 0
while x > 0:
    y += t[x % 16]
    x //= 16
print(y)

