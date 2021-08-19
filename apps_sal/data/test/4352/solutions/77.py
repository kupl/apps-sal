(A, B) = list(map(int, input().split()))
result = 'Alice'
if A == B:
    result = 'Draw'
elif A < B:
    if A == 1:
        result = 'Alice'
    else:
        result = 'Bob'
elif B == 1:
    result = 'Bob'
print(result)
