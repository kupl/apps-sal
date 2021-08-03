n = int(input())

wrest1 = []
wrest2 = []

sum1 = 0
sum2 = 0
l = 0

for i in range(n):
    a = int(input())
    if a > 0:
        wrest1.append(a)
        sum1 += a
        l = 'first'
    else:
        a = -a
        wrest2.append(a)
        sum2 += a
        l = 'second'

if sum1 > sum2:
    print('first')
elif sum2 > sum1:
    print('second')
else:
    winner = 0
    for i in range(min(len(wrest1), len(wrest2))):
        if wrest1[i] > wrest2[i]:
            winner = 1
            break
        elif wrest2[i] > wrest1[i]:
            winner = -1
            break
    if winner == 1:
        print('first')
    elif winner == -1:
        print('second')
    else:
        print(l)
