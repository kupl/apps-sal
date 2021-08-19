n = int(input())
a = []
b = []
last = 0
for i in range(n):
    x = int(input())
    if x > 0:
        a.append(x)
    else:
        b.append(-x)
    last = x
if sum(a) > sum(b):
    print('first')
elif sum(b) > sum(a):
    print('second')
elif a > b:
    print('first')
elif a < b:
    print('second')
elif last > 0:
    print('first')
elif last < 0:
    print('second')
