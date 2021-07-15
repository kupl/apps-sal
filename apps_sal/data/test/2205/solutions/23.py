from functools import reduce
from operator import xor
from itertools import accumulate

n, a = int(input()), list(map(int, input().split()))
arr, mem = [0], list(accumulate([i for i in range(n + 1)], lambda x, y: x ^ y))


if n > 1:
    if n % 2:
        arr.append(0 if (n // 2) % 2 else 1)
    else:
        arr.append(0 if ((n - 1) // 2) % 2 else 1)

for i in range(3, n + 1):
    if n % i == 0:
        arr.append(mem[i - 1] if (n // i) % 2 else 0)
    else:
        arr.append(mem[n % i] ^ mem[i - 1] if (n // i) % 2 else mem[n % i])

# print(arr)
print(reduce(xor, arr) ^ reduce(xor, a))

