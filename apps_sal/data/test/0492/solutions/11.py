(start, end) = input().split()
n = int(input()) % 4
if start == 'v':
    start = 0
elif start == '<':
    start = 1
elif start == '^':
    start = 2
elif start == '>':
    start = 3
if end == 'v':
    end = 0
elif end == '<':
    end = 1
elif end == '^':
    end = 2
elif end == '>':
    end = 3
temp1 = (4 + end - start) % 4
temp2 = (4 + start - end) % 4
if temp1 == temp2 == n:
    print('undefined')
elif temp1 == n:
    print('cw')
elif temp2 == n:
    print('ccw')
else:
    print('ERROR')
