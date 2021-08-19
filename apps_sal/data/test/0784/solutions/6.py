(a, b) = map(int, input().split())
ans = []
f = True
while b >= a:
    ans.append(b)
    if b % 10 == 1:
        b //= 10
    elif b % 2 == 0:
        b //= 2
    else:
        if b != a:
            f = False
        break
if ans[-1] != a:
    print('NO')
else:
    print('YES')
    print(len(ans))
    print(*ans[::-1])
