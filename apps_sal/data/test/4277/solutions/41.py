N, A, B = map(int, input().split())

train = N * A

if train <= B:
    print(train)
else:
    print(B)
