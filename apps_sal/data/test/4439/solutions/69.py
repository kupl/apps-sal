A, B = [int(input()) for _ in range(2)]
print(list(set([1, 2, 3]) - set([A, B]))[0])
