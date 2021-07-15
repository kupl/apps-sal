a, b = list(map(int, input().split()))
ans = [b]
while (b % 10 == 1 or b % 2 == 0) and b > 0 and b > a:
    if b % 2 == 0:
        b //= 2
        ans.append(b)
    elif b % 10 == 1 and b != 1:
        b = int(str(b)[:-1])
        ans.append(b)
    elif b == 1:
        ans.append(1)
        break
    
if a == b:
    print('YES')
    print(len(ans))
    print(*(reversed(ans)))
else:
    print('NO')

