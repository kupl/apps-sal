import math


def prime(num):
    array = []
    tmp = int(math.sqrt(n)) + 1
    for i in range(2, tmp):
        while num % i == 0:
            num /= i
            array.append(i)

    if array == []:
        return [num]
    else:
        if num > 1:
            array.append(int(num))
        return array


n = int(input())
P = prime(n)
P = sorted(P)
num = n
if 1 in P:
    print(0)
else:
    ans = 0
    tmp = 0
    for i in range(0, len(P)):
        if i == 0:
            tmp = P[i]
        elif P[i] == P[i - 1]:
            tmp *= P[i]
        else:
            tmp = P[i]
            num = n
        if num % tmp == 0:
            num /= tmp
            ans += 1

    print(ans)
