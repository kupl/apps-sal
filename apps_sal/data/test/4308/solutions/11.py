(N, K) = (int(x) for x in input().split())
s = N % K
if s == 0:
    print('0')
else:
    print('1')
