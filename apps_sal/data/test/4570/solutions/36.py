N, A, B = map(int, input().split())

if A * N < B:
    answer = A * N
else:
    answer = B
print(answer)
