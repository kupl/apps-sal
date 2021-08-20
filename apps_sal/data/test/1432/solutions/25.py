n = int(input())
A = list(map(int, input().split()))
answers = [0] * n
answers[n - 1] = sum(A) // 2 - sum(A[0:n - 1:2])
for i in range(n - 2, -1, -1):
    answers[i] = A[i] - answers[i + 1]
print(*[2 * a for a in answers])
