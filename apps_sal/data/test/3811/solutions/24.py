import math


def is_prime(n):
    if n == 1:
        return False
    if n == 2:
        return True
    for i in range(2, math.ceil(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True


def solve(arr):
    orig = []
    if is_prime(arr[0][0]) and arr[0][0] > 1:
        orig.append(arr[0][0])
    if is_prime(arr[0][1]) and arr[0][1] > 1:
        orig.append(arr[0][1])
    for i in range(2, math.ceil(math.sqrt(arr[0][0])) + 1):
        if arr[0][0] % i == 0:
            if is_prime(i):
                orig.append(i)
            if arr[0][0] // i > 1 and is_prime(arr[0][0] // i):
                orig.append(arr[0][0] // i)
    for i in range(2, math.ceil(math.sqrt(arr[0][1])) + 1):
        if arr[0][1] % i == 0:
            if is_prime(i):
                orig.append(i)
            if arr[0][1] // i > 1 and is_prime(arr[0][1] // i):
                orig.append(arr[0][1] // i)
    for el in arr:
        orig = [i for i in orig if el[0] % i == 0 or el[1] % i == 0]
    return -1 if len(orig) == 0 else orig[0]


n = int(input().strip())
a = []
for i in range(n):
    a.append([int(x) for x in input().strip().split()])
print(solve(a))
