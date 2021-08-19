(a, b, c) = list(map(int, input().strip().split()))
a = a % b
for i in range(10 * b):
    a *= 10
    d = a // b
    a = a % b
    if c == d:
        print(i + 1)
        break
else:
    print(-1)
