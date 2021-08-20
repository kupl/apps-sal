(A, B, C) = list(map(int, input().split()))
result = 'No'
if A <= C <= B:
    result = 'Yes'
print(result)
