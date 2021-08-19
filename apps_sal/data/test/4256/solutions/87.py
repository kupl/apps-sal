(A, B, C) = list(map(int, input().split()))
if A * C <= B:
    answer = C
else:
    answer = B // A
print(answer)
