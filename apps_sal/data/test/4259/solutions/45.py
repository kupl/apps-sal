K = int(input())
A, B = list(map(int, input().split()))
if B // K * K >= A:
    print('OK')
else:
    print('NG')
