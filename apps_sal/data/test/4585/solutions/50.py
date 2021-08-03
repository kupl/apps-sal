X = int(input())
X2 = X * 2
k = 1
while True:
    if k * (k + 1) >= X2:
        print(k)
        return
    k += 1
