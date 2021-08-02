
n, k = list(map(int, input().split()))
i = 0
a = []

while n != 0:
    a.append(n % k)

    n = n // k
    i = i + 1

print((len(a)))
