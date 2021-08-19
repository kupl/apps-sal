K = int(input())
(A, B) = list(map(int, input().split()))
if B // K - A // K >= 1:
    print('OK')
elif B % K == 0:
    print('OK')
elif A % K == 0:
    print('OK')
else:
    print('NG')
