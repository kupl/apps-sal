n = int(input())
a = [0]*11
if n < 4:
    a[0] = n
    n = 0
else:
    a[0] = 4
    n -= 4
    i = 1
    while n > 0:
        if n < 3:
            a[i] = n
            n = 0
        else:
            a[i] = 3
            n -= 3
        i+=1

def pb(x):
    nonlocal a
    for i in a[1:]:
        print('O' if i >= x else '#', end='.')
print('+------------------------+')
print(end='|'); print('O' if a[0] >= 1 else '#', end='.'); 
pb(1); print('|D|)')
print(end='|'); print('O' if a[0] >= 2 else '#', end='.'); 
pb(2); print('|.|')
print(end='|'); print('O' if a[0] >= 3 else '#', end=''); print('.......................|')
print(end='|'); print('O' if a[0] >= 4 else '#', end='.'); 
pb(3); print('|.|)')
print('+------------------------+')

