k = int(input())
(a, b) = map(int, input().split())
largest = b // k * k
if a <= largest:
    print('OK')
else:
    print('NG')
