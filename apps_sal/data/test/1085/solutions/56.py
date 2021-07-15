# coding: utf-8
import sys

sr = lambda: sys.stdin.readline().rstrip()
ir = lambda: int(sr())
lr = lambda: list(map(int, sr().split()))

N = ir()
# 候補はNかN-1の約数
answer = 0

def make_divisors(n):  # nの約数を列挙
    divisors = []
    for i in range(1, int(n**0.5)+1):
        if n % i == 0:
            divisors.append(i)
            if i != n // i:
                divisors.append(n//i)
    divisors.sort()
    return divisors[1:]

cand = make_divisors(N) + make_divisors(N-1)
for x in cand:
    M = N
    while M % x == 0:
        M //= x
    r = M % x
    if r == 1:
        answer += 1

print(answer)

