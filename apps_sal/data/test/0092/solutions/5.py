# 236B

import math

arr = list(map(int, input().split(" ")))
a = arr[0]
b = arr[1]
c = arr[2]

d = dict()


def numdiv(n):
    if n in d:
        return d[n]
    else:
        count = 0
        for i in range(1, int(math.sqrt(n) + 1)):
            if n % i == 0:
                count += 2
        if int(math.sqrt(n)) * int(math.sqrt(n)) == n:
            count -= 1
        d[n] = count
        return count


answer = 0
for i in range(1, a + 1):
    for j in range(1, b + 1):
        for k in range(1, c + 1):
            answer += numdiv(i * j * k)

print(answer)
