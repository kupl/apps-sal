a, b = [int(i) for i in input().split()]
iters = 0
while a <= b:
    a *= 3
    b *= 2
    iters += 1
print(iters)
