number = input().split(' ')
D = int(number[0])
T = int(number[1])
S = int(number[2])
time = D / S
if time <= T:
    print('Yes')
else:
    print('No')
