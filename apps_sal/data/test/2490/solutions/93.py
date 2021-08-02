N = input()

over = 1
eq = 0

for n in map(int, N):
    o = min(eq + n + 1, over + (10 - n) - 1)
    e = min(eq + n, over + (10 - n))

    over = o
    eq = e

print(eq)
