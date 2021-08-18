X = int(input())
a = 0
X_ri = round(pow(X, 1 / 2))

if X == 2:
    print(2)
    return
if X % 2 == 0:
    X = X + 1

while True:
    for i in range(3, X_ri + 1, 2):
        if X % i == 0:
            break
    else:
        print(X)
        break
    X = X + 2
