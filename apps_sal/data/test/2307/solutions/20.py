import sys
n = eval(input())


def even(a):
    a = int(a)
    if a % 2 == 0:
        return 1
    return 0


a = list(map(even, sys.stdin.readline().split()))
if a.count(1) > len(a) / 2:
    print('READY FOR BATTLE')
else:
    print('NOT READY')
