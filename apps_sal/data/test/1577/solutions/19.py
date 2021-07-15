n = int(input())
s = input()
A = 0
D = 0
for i in s:
    if i == 'A':
        A += 1
    else:
        D += 1
if A > D:
    print('Anton')
elif D > A:
    print('Danik')
else:
    print('Friendship')

