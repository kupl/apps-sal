k = int(input())
a, b = list(map(int, input().split()))
if b // k > a // k or a % k == 0:
    print('OK')
else:
    print('NG')

