n = int(input())
u, v = 0, 0
for _ in range(n):
    x, y = list(map(int, input().split(' ')))
    if x > y:
        u += 1
    elif x < y:
        v += 1

if u > v:
    print('Mishka')
elif u < v:
    print('Chris')
else:
    print('Friendship is magic!^^')

