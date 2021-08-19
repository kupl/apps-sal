y = [int(i) for i in input().split()]
N = y[0]
Q = y[1]
if Q & 1:
    print('No')
elif Q >= N * 2 and Q <= N * 4:
    print('Yes')
else:
    print('No')
