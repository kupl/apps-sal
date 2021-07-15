n, k = list(map(int, input().split()))
xs = list(map(int, input().split()))

i = 0
while k > 0:
    i += 1
    h = k
    k -= i

print(xs[h - 1])

