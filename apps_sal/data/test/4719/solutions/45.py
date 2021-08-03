n = int(input())
S = list(input() for _ in range(n))

T = "abcdefghijklmnopqrstuvwxyz"
for c in T:
    x = 50
    for s in S:
        x = min(x, s.count(c))
    print(c * x, end='')
print()
