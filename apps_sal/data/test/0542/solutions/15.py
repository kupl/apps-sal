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
else:
    ok1 = 0
    for i in range(min(len(a), len(b))):
        if a[i] > b[i]:
            ok1 = 1
            break
        elif a[i] < b[i]:
            ok1 = 2
            break
    if ok1 == 1:
        print('first')
    elif ok1 == 2:
        print('second')
    else:
        if last == 1:
            print('first')
        if last == 2:
            print('second')
