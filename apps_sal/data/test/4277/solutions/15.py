(n, a, b) = list(map(int, input().split()))
train = n * a
taxi = b
if train < taxi:
    print(train)
else:
    print(taxi)
