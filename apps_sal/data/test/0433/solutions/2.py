
try:
    while True:
        n, a, b = list(map(int, input().split()))
        x = (a + b) % n
        print(n if x == 0 else x)

except EOFError:
    pass
