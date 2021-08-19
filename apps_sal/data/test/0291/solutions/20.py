(a, b) = list(map(int, input().split()))
for i in range(10):
    if 3 ** i * a > 2 ** i * b:
        print(i)
        break
