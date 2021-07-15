K = int(input())
A, B = map(int, input().split())

if K * (A // K + 1) <= B or A % K == 0 or B % K == 0:
    print('OK')
else:
    print('NG')
