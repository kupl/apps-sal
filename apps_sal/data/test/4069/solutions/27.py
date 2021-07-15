x,num,dis = map(int,input().split())

if x < 0:
    x = x*-1
n =  x//dis + 1

if num < n:
    print(abs(x-num*dis))
elif (num - n) % 2 == 0:
    print(abs(x-dis*n))
else:
    print(abs(x-dis*(n-1)))
