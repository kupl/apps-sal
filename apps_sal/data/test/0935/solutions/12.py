istr = input()
[x,y] = istr.split(' ')
n = int(x)
m = int(y)
prod = n*m;
c = 0
while(n*m > 0):
    c=c+1
    n = n-1
    m =m-1
if(c %2 == 1):
    print('Akshat')
else:
    print('Malvika')

