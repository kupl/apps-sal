t = int(input())
for _ in range(t):
    a, b = list(map(int, input().split()))

    x = len(str(b))
    if not all(k == '9' for k in str(b)):
        x -= 1
    print(a * x)

