(n, m) = list(map(int, input().split()))
steps = [m]
while m > n:
    if m % 2 == 0:
        m //= 2
    elif m % 10 == 1:
        m //= 10
    else:
        break
    steps.append(m)
if m != n:
    print('NO')
else:
    print('YES')
    steps.reverse()
    print(len(steps))
    print(*steps)
