n = int(input())
a = [int(input()) for _ in range(5)]
minimum = min(a)
print((n + minimum - 1) // minimum + 4)
