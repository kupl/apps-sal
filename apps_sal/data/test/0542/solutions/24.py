num = int(input().split('\n')[0])

first = []
second = []
last_move = 0
for i in range(num):
    next = int(input().split('\n')[0])
    if next > 0:
        first.append(next)
        if i == num - 1:
            last_move = 'first'
    else:
        second.append(-next)
        if i == num - 1:
            last_move = 'second'

if sum(first) > sum(second):
    print('first')
elif sum(second) > sum(first):
    print('second')
else:
    if first > second:
        print('first')
    elif second > first:
        print('second')
    else:
        print(last_move)
