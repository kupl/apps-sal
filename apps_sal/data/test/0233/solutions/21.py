n = int(input())
m = 0
c = 0
for i in range(n):
    x, y = map(int, input().split())
    if x > y:
        m += 1
    elif x < y:
        c += 1
if m > c:
    print('Mishka')
elif m < c:
    print('Chris')
else:
    print('Friendship is magic!^^')
