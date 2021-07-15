n = int(input())
a = [int(i) for i in input().split()]
b = [int(i) for i in input().split()]
s = sum(a)
b.sort(reverse = True)
if b[0] + b[1] >= s:
    print('YES')
else:
    print('NO')

