
A, B = list(map(int, input().split()))

answer = max(A + B, A - B, A * B)

print(answer)
