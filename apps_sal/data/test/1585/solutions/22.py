X, Y = list(map(int, input().split()))

i = 1
while Y >= 2**i * X:
    i = i + 1
print(i)
