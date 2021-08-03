n = int(input())
A = [0] * n
for i in range(n):
    per = int(input())
    A[i] = per
A.sort()
answer = 0
for i in range(n):
    answer = (answer + A[i] * A[n - i - 1]) % 10007
print(answer)
