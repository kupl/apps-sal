import math
(a, b) = [int(i) for i in input().split()]
if a < b:
    print(0)
elif a == b:
    print('infinity')
else:

    def FindAllDivisors(x, b):
        y = 1
        ans = []
        while y <= int(math.sqrt(x)):
            if x % y == 0:
                if y != int(x / y):
                    if y > b:
                        ans.append(y)
                    if int(x / y) > b:
                        ans.append(int(x / y))
                elif y == int(x / y) and y > b:
                    ans.append(y)
            y += 1
        return len(ans)
    print(FindAllDivisors(a - b, b))
