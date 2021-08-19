n = int(input())
a = sum(list(map(int, input().split())))
b = sum(list(map(int, input().split())))
if b <= a:
    print('Yes')
else:
    print('No')
