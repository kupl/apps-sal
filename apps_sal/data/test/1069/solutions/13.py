n = int(input())
out = (1 + pow(2, n, 5) + pow(3, n, 5) + pow(4, n, 5)) % 5
print(out)
