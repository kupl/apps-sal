(X, Y) = map(int, input().split())
A = [X]
while True:
    next = A[-1] * 2
    if next > Y:
        break
    else:
        A.append(next)
print(len(A))
