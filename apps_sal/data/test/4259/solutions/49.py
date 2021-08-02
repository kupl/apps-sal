k = int(input())
a, b = map(int, input().split())
if ((b - a) >= k):
    print('OK')
elif (a % k == 0) or (b % k == 0):
    print('OK')
elif(a < (a // k) * k + k < b):
    print('OK')
else:
    print('NG')
