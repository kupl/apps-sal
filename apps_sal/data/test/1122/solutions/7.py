(N, M) = list(map(int, input().split()))
a = 1
b = 1 + M
while a < b:
    print(a, b)
    a += 1
    b -= 1
a = M + 2
b = 2 * M + 1
while a < b:
    print(a, b)
    a += 1
    b -= 1
