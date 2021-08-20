X = int(input())
if X == 2:
    print(X)
else:
    while 1:
        if X % 2 == 0:
            X += 1
            continue
        else:
            for i in range(3, X):
                if X % i == 0:
                    break
            else:
                print(X)
                break
            X += 1
            continue
