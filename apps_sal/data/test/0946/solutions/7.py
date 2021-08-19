n = int(input())
a = list(map(int, input().split()))
if a.count(1) > 0:
    print('HARD')
else:
    print('EASY')
