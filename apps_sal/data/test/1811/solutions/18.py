(n, k) = list(map(int, input().split()))
if max(list(map(len, input().split('.')))) < k:
    print('YES')
else:
    print('NO')
