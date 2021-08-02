def solve():
    n = int(input())
    t = 2
    while True:
        k = 2**t - 1
        if n % k == 0:
            return n // k
        t += 1


# ----
t = int(input())
for case in range(t):
    print(solve())
