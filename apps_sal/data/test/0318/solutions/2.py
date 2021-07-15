h, m = [int(x) for x in input().split(':')]
a = int(input())
x = h * 60 + m + a
x = x % (60 * 24)

print(x // 600, x // 60 % 10, ':', x % 60 // 10, x % 60 % 10, sep='')

