from collections import Counter
n = int(input())
c = Counter(list(map(int, input().split())))
if c[1] == 0:
    print('2 ' * c[2])
elif c[2] == 0:
    print('1 ' * c[1])
else:
    print('2 1 ' + '2 ' * (c[2] - 1) + '1 ' * (c[1] - 1))
