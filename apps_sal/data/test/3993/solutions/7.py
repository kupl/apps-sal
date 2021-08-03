import math
import collections


def func(a, k):
    if a % k != 0:
        mod = 1
    else:
        mod = 0
    return math.floor(a / k) * k + mod * k


n, m, k = input().split()
list = input().split()
k = int(k)
temp = k
size = 0
answer = 0
c = 0
c2 = 0
check = 'false'
used = 0

temp = func(int(list[0]), k)
for i in range(len(list)):
    list[i] = int(list[i])
    used = 0
    if list[i] <= temp:
        c += 1
        check = 'true'
        used = 1
    if list[i] >= temp:
        if check is 'true':
            answer += 1
            check = 'false'
            temp += c
            c = 0
            if list[i] - c <= temp and used == 0:
                c += 1
                check = 'true'
                used = 1
            else:
                temp = temp + func(int(list[i]) - temp, k)
                if list[i] - c <= temp and used == 0:
                    c += 1
                    check = 'true'
                    used = 1
        elif check is 'false':
            temp = temp + func(int(list[i]) - temp, k)
            if list[i] - c <= temp and used == 0:
                c += 1
                check = 'true'
                used = 1


print(answer if check is 'false' else answer + 1)
