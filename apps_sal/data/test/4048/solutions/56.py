N = int(input())
d = 10**20
for a in range(1, int(N ** 0.5) + 1):
    if N % a == 0:
        b = N // a
        c = a + b - 2
        if d > c:
            d = c
print(d)
