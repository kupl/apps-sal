input(); a = list(map(int, input().split())); r = float('inf')
for i in range(min(a), max(a) + 1):
    n = 0
    for j in a:
        n += (j - i)**2
    r = min(n, r)
print(r)
