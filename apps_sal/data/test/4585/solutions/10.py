def solve():
    X = int(input())
    now = 0
    for i in range(X + 1):
        now += i
        if now >= X:
            return i

print((solve()))

