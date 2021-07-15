n, k = list(map(int, input().split()))
a = list(map(int, input().split()))
m = min(enumerate(a), key=lambda l: n % l[1])
print(m[0] + 1, n // m[1])

