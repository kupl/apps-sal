(n, b, d) = map(int, input().split())
A = list(map(int, input().split()))
answer = 0
bal = 0
for i in range(n):
    if A[i] <= b:
        bal += A[i]
        if bal > d:
            bal = 0
            answer += 1
print(answer)
