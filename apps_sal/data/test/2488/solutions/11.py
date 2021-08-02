# 素数関連
from collections import deque


def prime_numbers(x):
    if x < 2:
        return []
    prime_numbers = [i for i in range(x)]
    prime_numbers[1] = 0
    for prime_number in prime_numbers:
        if prime_number > math.sqrt(x):
            break
        if prime_number == 0:
            continue
        for composite_number in range(2 * prime_number, x, prime_number):
            prime_numbers[composite_number] = 0
    return [prime_number for prime_number in prime_numbers if prime_number != 0]


def is_prime(x):
    if x < 2:
        return False
    if x == 2 or x == 3 or x == 5:
        return True
    if x % 2 == 0 or x % 3 == 0 or x % 5 == 0:
        return False
    prime_number = 7
    difference = 4
    while prime_number <= math.sqrt(x):
        if x % prime_number == 0:
            return False
        prime_number += difference
        difference = 6 - difference
    return True


n, d, a = map(int, input().split())
xh = [list(map(int, input().split())) for i in range(n)]
xh.sort()
queue = deque()
ans = 0
cur = 0
for i in range(n):
    x, h = xh[i]
    while queue != deque() and queue[0][0] < x:
        cur -= queue.popleft()[1]
    h -= cur
    if h > 0:
        cur += a * ((h - 1) // a + 1)
        ans += (h - 1) // a + 1
        queue.append([x + 2 * d, a * ((h - 1) // a + 1)])
print(ans)
