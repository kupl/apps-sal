lst = list(map(int, input().split()))
n=lst[0]
m=lst[1]
small=n if n<m else m
if small%2==0:
    print('Malvika')
else:
    print('Akshat')

