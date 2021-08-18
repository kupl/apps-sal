K = int(input())
A, B = map(int, input().split())
K_max = int(B / K) * K
if A <= K_max:
    print('OK')
else:
    print('NG')
