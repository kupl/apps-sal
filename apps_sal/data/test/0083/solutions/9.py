n = int(input())
a = list(map(int, input().split()))
pos = sum((x > 0 for x in a))
neg = sum((x < 0 for x in a))
needed = (n + 1) // 2
if pos >= needed:
    print('1')
elif neg >= needed:
    print('-1')
else:
    print(0)
