
try:
    while True:
        n = int(input())
        print("".join(map(str, list(range(1, n + 1))))[n - 1])

except EOFError:
    pass
