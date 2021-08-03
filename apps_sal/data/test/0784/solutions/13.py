a, b = list(map(int, input().split()))
arr = [str(b)]
while b > a:
    if b % 10 == 1:
        b //= 10
        arr.append(str(b))
    elif b % 2 == 0:
        b //= 2
        arr.append(str(b))
    else:
        b = -1
if b == a:
    arr.reverse()
    print('YES', len(arr), ' '.join(arr), sep='\n')
else:
    print('NO')
