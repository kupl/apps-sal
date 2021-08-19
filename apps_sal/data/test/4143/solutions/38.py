n = int(input())
l = [int(input()) for i in range(5)]
mi = min(l)
print((n + mi - 1) // mi + 4)
