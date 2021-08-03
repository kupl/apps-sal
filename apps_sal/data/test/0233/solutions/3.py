n = int(input())
m, c = 0, 0

for i in range(n):
    a, b = [int(x) for x in input().split(' ')]
    if a > b:
        m += 1
    elif a < b:
        c += 1

if m > c:
    print('Mishka')
elif m < c:
    print('Chris')
else:
    print('Friendship is magic!^^')
