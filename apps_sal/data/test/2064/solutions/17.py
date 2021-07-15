n = int(input())
if(n % 2 != 0):
    n -= 3
    print('7', end='')
while(n!=0):
    n -= 2
    print('1', end='')
