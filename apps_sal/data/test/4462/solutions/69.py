n = int(input())
a_list = list(map(int, input().split()))
x = y = z = 0
for a in a_list:
    if a % 4 == 0:
        x += 1
    elif a % 2 == 0:
        y += 1
    else:
        z += 1
if y == 0 and x >= z - 1 or (y > 0 and x >= z):
    print('Yes')
else:
    print('No')
