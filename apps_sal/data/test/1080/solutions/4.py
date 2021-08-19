n = int(input())
a = list(map(int, input().split()))
sum1 = sum(a)
max1 = max(a)
if sum1 % 2 == 0 and sum1 - max(a) >= max(a):
    print('YES')
else:
    print('NO')
