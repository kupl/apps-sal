(n, a, b) = list(map(int, input().split()))
c = (n * 100 + a + b) % n
print([c, n][c == 0])
