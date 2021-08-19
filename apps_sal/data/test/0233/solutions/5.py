b1 = 0
b2 = 0
for i in range(int(input())):
    (a, b) = map(int, input().split())
    if a > b:
        b1 += 1
    elif b > a:
        b2 += 1
if b1 > b2:
    print('Mishka')
elif b2 > b1:
    print('Chris')
else:
    print('Friendship is magic!^^')
