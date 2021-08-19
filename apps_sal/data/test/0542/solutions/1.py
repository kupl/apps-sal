n = int(input())
a = []
b = []
sum_a = 0
sum_b = 0
last = ''
for i in range(n):
    x = int(input())
    if x > 0:
        sum_a += x
        a.append(x)
        last = 'first'
    else:
        sum_b -= x
        b.append(-x)
        last = 'second'
if sum_a > sum_b:
    print('first')
elif sum_b > sum_a:
    print('second')
elif a > b:
    print('first')
elif b > a:
    print('second')
else:
    print(last)
