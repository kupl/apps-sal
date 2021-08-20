(a, b) = map(int, input().split())
pred = [str(b)]
while a != b and b > a:
    if b % 10 == 1 and b != 1:
        b = b // 10
        pred.append(str(b))
    elif b % 2 == 0:
        b = b // 2
        pred.append(str(b))
    else:
        break
if a != b:
    print('NO')
else:
    print('YES')
    print(len(pred))
    pred.reverse()
    print(' '.join(pred))
