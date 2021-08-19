array = list(map(str, input().split()))
if array.count('5') == 2 and array.count('7') == 1:
    print('YES')
else:
    print('NO')
