def inputlist():
    return [int(j) for j in input().split()]


(X, A) = inputlist()
if X < A:
    print('0')
else:
    print(10)
