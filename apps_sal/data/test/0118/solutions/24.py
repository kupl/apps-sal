T,S,X = list(map(int,input().split()))


#T, T+1(X)
#T, T+1  // +S*k

if X<T:
    print('NO')
elif (X - T) % S == 1 or (X - T) % S == 0:
    if X == T+1:
        print('NO')
    else:
        print("YES")
else:
    print('NO')

