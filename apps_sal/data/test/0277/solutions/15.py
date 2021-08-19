(n, a, b) = map(int, input().split())
num = 0
a += n - 2
b += n - 2
while a != b:
    a = (a - 1) // 2
    b = (b - 1) // 2
    num += 1
if 2 ** num == n:
    print('Final!')
else:
    print(num)
