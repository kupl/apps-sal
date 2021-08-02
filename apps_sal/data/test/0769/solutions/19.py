from functools import lru_cache

a, b, c = tuple(map(int, input().split()))
a *= 10
k = 0
flag = True

while flag:
    k += 1

    d = a // b
    a = (a % b) * 10
    if c == d:
        flag = False
        print(k)

    if k > 100000:
        print(-1)
        flag = False
