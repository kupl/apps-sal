n = int(input())
first = []
second = []
last = 0
for i in range(n):
    a = int(input())
    if a > 0:
        first.append(a)
    else:
        second.append(abs(a))
    if i == n - 1:
        last = a
if abs(sum(first)) > abs(sum(second)):
    print('first')
    quit()
if abs(sum(first)) < abs(sum(second)):
    print('second')
else:
    if first > second:
        print('first')
        quit()
    if first < second:
        print('second')
    elif last > 0:
        print('first')
    else:
        print('second')
