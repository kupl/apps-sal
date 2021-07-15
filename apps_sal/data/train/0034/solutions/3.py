T = int(input())
for kase in range(T):
    n = int(input())
    if n&1:
        print('7'+(n-3)//2*'1')
    else:
        print(n//2*'1')
