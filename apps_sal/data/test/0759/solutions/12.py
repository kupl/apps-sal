import math
arr = list(map(str, input().strip().split(' ')))
n = int(arr[0])
t = int(arr[1])

h, d, c, nn = (list(map(int, input().strip().split(' '))))
if(n >= 20):
    price = .8 * c * math.ceil(h * 1.0 / nn * 1.0)
    print(price)
else:
    hunger = (20 * 60 - n * 60 - t) * d + h
    price = min(.8 * c * math.ceil(hunger * 1.0 / nn * 1.0), math.ceil(h * 1.0 / nn * 1.0) * c)
    print(price)
