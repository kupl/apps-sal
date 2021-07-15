n = int(input().strip())
cycles = list(map(int, input().strip().split()))

n_steps = 0
for c in cycles:
    n_steps += c - 1
    print(int(not(n_steps % 2)) + 1)

