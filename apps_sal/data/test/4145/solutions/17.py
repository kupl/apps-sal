import math
X = int(input())
if X == 2:
    print(2)
else:
    is_end = False
    while not is_end:
        is_end = True
        for i in range(2, X // 2):
            if math.gcd(i, X) != 1:
                is_end = False
                X += 1
                break
    print(X)
