(s, f) = input().split()
n = int(input())
spinner = ['v', '<', '^', '>']
if spinner[(spinner.index(s) + n) % 4] == spinner[(spinner.index(s) - n) % 4] == f:
    print('undefined')
elif spinner[(spinner.index(s) + n) % 4] == f:
    print('cw')
else:
    print('ccw')
