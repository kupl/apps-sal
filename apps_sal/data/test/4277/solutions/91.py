N, A, B = map(int, input().split())

train = A * N
taxi = B

if train >= taxi:
    print(taxi)
else:
    print(train)
