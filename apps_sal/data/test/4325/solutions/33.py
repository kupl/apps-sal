(N, X, T) = map(int, input().split())
check = N % X
kaisu = N // X
if check == 0:
    print(kaisu * T)
else:
    print((kaisu + 1) * T)
