n = int(input())
arr=[]
if n==0:
    arr.append(0)
else:
    while n > 0:
        arr.append(n % 10)
        n=n //10
for i in range(len(arr)):
    if arr[i]<5:
        print('O-|', end = '')
        for j in range(arr[i]):
            print('O', end = '')
        print('-', end = '')
        for j in range(4-arr[i]):
            print('O', end = '')
    if arr[i]==5:
        print('-O|-OOOO', end = '')
    if arr[i]>5:
        print('-O|', end = '')
        for j in range(arr[i]-5):
            print('O', end = '')
        print('-', end = '')
        for j in range(9-arr[i]):
            print('O', end = '')
    if i != len(arr)-1:
        print('')
