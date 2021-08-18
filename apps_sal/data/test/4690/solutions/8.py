
A, B, C, D = map(int, input().split())


if A * B >= C * D:
    answer = A * B
else:
    answer = C * D

print(answer)
