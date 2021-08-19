(T, S, X) = list(map(int, input().split()))
if X < T:
    print('NO')
elif (X - T) % S == 1 or (X - T) % S == 0:
    if X == T + 1:
        print('NO')
    else:
        print('YES')
else:
    print('NO')
