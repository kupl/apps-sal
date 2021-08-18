
try:
    while True:
        n = int(input())
        a = list(map(int, input().split()))
        m = max(a)
        print((m << 1) - sum(a) + 1)

except EOFError:
    pass
