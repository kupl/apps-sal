from math import sqrt
n = int(input().strip())
s = set()


def f(n):
    return n * (n + 1) // 2


for i in range(1, int(sqrt(n)) + 1):
    if(n % i == 0):
        x = i * f(n // i - 1) + n // i
        s.add(x)

        j = n // i
        y = j * f(n // j - 1) + n // j
        s.add(y)
        #print(i, j, x,y)

print(" ".join(map(str, sorted(list(s)))))
