K = int(input())
A, B = map(int, input().split())
C = A // K
D = B // K
E = A % K
F = B % K
if E == 0 or F == 0:
    print('OK')
elif C == D:
    print('NG')
else:
    print('OK')
