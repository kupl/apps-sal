t = int(input())
for _ in range(t):
    a, b = list(map(int, input().split()))
    x = len(str(b))
    if b != int('9' * x):
        x -= 1
    print(a * x)

