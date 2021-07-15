from math import sqrt

def f(x):
    divisors = [[], []]
    for i in range(1, int(sqrt(x))+1):
        if x % i == 0:
            divisors[0].append(i)
            if i * i != x:
                divisors[1].append(x//i)
    return divisors[0] + divisors[1][::-1]

n, m = map(int, input().split())
for i in f(m):
    if n <= i:
        print(m//i)
        return
