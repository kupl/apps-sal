k = int(input())
(a, b) = list(map(int, input().split()))
if b < k * (a // k + 1) and a % k != 0:
    print('NG')
else:
    print('OK')
