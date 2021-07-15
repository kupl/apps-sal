a = [int(input()) for i in range(5)]
b = [9 - (i - 1) % 10 for i in a]
print(sum(a) + sum(b) - max(b))
