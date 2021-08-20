n = int(input())
a = [int(i) for i in input().split()]
if len(a) % 2 and a[0] % 2 and a[-1] % 2:
    print('Yes')
else:
    print('No')
