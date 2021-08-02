n = int(input())
a = [int(s) for s in input().split()]
if a.count(1) >= 1:
    print('HARD')
else:
    print('EASY')
