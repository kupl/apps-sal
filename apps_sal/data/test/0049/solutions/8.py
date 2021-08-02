def mp():
    return map(int, input().split())


def f(i):
    return (10 ** i - 10 ** (i - 1)) * i


n = int(input())

i = 1
sum = 0
while n - f(i) >= 0:
    n -= f(i)
    sum += f(i) // i
    i += 1

print(str(sum + (n + i - 1) // i)[n % i - 1])
