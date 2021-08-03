a, b = input().split()
n = int(input())
n = n % 4
V = ['^', '>', 'v', '<']
i = 0
while a != V[i]:
    i += 1
ti = (i + 4 - n) % 4
i = (i + n) % 4
if b == V[i] and b == V[ti]:
    print('undefined')
elif b == V[i]:
    print('cw')
elif b == V[ti]:
    print('ccw')
else:
    print('undefined')
