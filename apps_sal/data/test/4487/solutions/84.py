(A, B, C) = list(map(str, input().split()))
initial_1 = A[-1]
end_1 = B[0]
initial_2 = B[-1]
end_2 = C[0]
if initial_1 == end_1 and initial_2 == end_2:
    print('YES')
else:
    print('NO')
