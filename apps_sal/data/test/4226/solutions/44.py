(X, Y) = map(int, input().split())
if Y % 2 == 1:
    print('No')
else:
    for num_turu in range(X + 1):
        num_kame = X - num_turu
        if Y == 4 * num_kame + 2 * num_turu:
            print('Yes')
            break
    else:
        print('No')
