from sys import stdin, stdout
import collections

N = int(input())


def is_prime(a):
    return all(a % i for i in range(2, a))


res = N

while not is_prime(res):
    res += 1

print(res)
for i in range(N - 1):
    print(i + 1, i + 2)

print(N, 1)

half = N // 2 + 1 * (N % 2 == 1)
for i in range(res - N):
    print(i + 1, i + 1 + half)
