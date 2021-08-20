k = int(input())
(a, b) = list(map(int, input().split()))
if b // k != a // k or b % k == 0 or a % k == 0:
    print('OK')
else:
    print('NG')
