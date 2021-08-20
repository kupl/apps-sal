k = int(input())
(a, b) = map(int, input().split())
if a % k == 0:
    n = a // k
else:
    n = a // k + 1
if k * n > b:
    print('NG')
else:
    print('OK')
