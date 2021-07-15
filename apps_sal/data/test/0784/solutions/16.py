a, b = map(int, input().split())
ans = [b]

while (b > a):
    if (b % 2 == 0):
        b //= 2
        ans.append(b)
    elif (b % 10 == 1):
        b //= 10
        ans.append(b)
    else:
        break

if (b == a):
    print('YES')
    print(len(ans))
    print(*reversed(ans))
else:
    print('NO')
