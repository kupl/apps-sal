N, A, B = list(map(int,input().split()))

train = N*A
taxi = B

if train < taxi:
    print(train)
else:
    print(taxi)

