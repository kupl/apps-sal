# import sys
# sys.stdin = open('cf598a.in')

def smaller_power(n):
    cpow = -1
    while n:
        n >>= 1
        cpow += 1
    return 1 << cpow


t = int(input())

for _ in range(t):
    n = int(input())
    sum_full = n * (n + 1) // 2
    sum_powers = (smaller_power(n) << 1) - 1
    print(sum_full - (sum_powers << 1))
