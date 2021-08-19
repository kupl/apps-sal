import math
n = int(input())
result = []


def divisors(n):
    count = 0
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            if n // i == i:
                count += 1
            else:
                count += 2
    return count


for i in range(n):
    n1 = int(input())
    n2 = list(list(map(int, input().split())))
    n2.sort()
    a1 = n2[0] * n2[-1]
    final = True
    for i in range(len(n2)):
        if n2[i] * n2[len(n2) - 1 - i] != a1:
            final = False
            break
    if n1 == 1 and n2[0] == 1:
        result.append(1)
    elif final and n1 == divisors(a1):
        result.append(a1)
    else:
        result.append(-1)
for i in result:
    print(i)
