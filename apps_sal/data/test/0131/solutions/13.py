n = int(input())
a = sum([int(i) for i in input().split()])
b = sum([int(i) for i in input().split()])
if a >= b:
    print('Yes')
else:
    print('No')
