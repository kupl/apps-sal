import sys


def factorize(n):
    if n == 2:
        return [2]
    b = 2
    fct = []
    while b * b <= n:
        while n % b == 0:
            n //= b
            fct.append(b)
        break
    return fct


input = sys.stdin.readline
n = int(input())
a_list = list(map(int, input().split()))
count_2 = 0
for a in a_list:
    count_2 += len(factorize(a))
print(count_2)
