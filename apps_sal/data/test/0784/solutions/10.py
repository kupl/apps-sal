(a, b) = list(map(int, input().split()))
ans = []
fl = False
ans.append(b)
while b > a:
    if b % 2 == 0:
        b //= 2
        ans.append(b)
    elif b % 10 == 1:
        b //= 10
        ans.append(b)
    else:
        fl = True
        print('NO')
        break
if not fl and b == a:
    print('YES')
    print(len(ans))
    print(*ans[::-1])
elif not fl:
    print('NO')
