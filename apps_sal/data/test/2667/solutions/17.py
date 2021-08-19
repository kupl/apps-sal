l = list()
n = int(input())
x = [int(item) for item in input().split()]
sum1 = sum(x)
j = 1
while n:
    l.append(j)
    j = j + 1
    n = n - 1
if sum1 == sum(l):
    print('YES')
else:
    print('NO')
