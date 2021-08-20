n = int(input())
a = []
b = []
last = 0
for i in range(n):
    q = int(input())
    if q > 0:
        a.append(q)
        last = 1
    else:
        b.append(-q)
        last = 2
sum1 = sum(a)
sum2 = sum(b)
if sum1 > sum2:
    print('first')
elif sum1 < sum2:
    print('second')
elif a > b:
    print('first')
elif b > a:
    print('second')
else:
    if last == 1:
        print('first')
    if last == 2:
        print('second')
