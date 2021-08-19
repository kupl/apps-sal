n = int(input())
A = list(map(int, input().split()))
answer = [0] * n
for i in range(len(A) - 1, -1, -1):
    if i == len(A) - 1:
        answer[i] = A[i]
    else:
        answer[i] = A[i] + A[i + 1]
print(' '.join(map(str, answer)))
