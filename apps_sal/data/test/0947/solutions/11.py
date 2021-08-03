import math
t = int(input())

for _ in range(t):
    n = int(input())
    ans = False
    for i in range(2, int(math.sqrt(n) + 1)):
        if n % i == 0:
            print(str(n // i) + ' ' + str(n - n // i))
            ans = True
            break
    if not ans:
        print('1 ' + str(n - 1))
