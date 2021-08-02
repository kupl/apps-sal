n = int(input())
A = list(map(int, input().split()))
A.sort()
for i in range(n):
    A[i] = [A[i], 0]
answer = 0
per2 = -float('infinity')
per = 0
for i in range(n - 1):
    if A[i][1] == 0:
        A[i][1] = 1
        per = A[i][0]
        for j in range(i + 1, n):
            if A[j][1] == 0:
                if A[j][0] > per:
                    per = A[j][0]
                    A[j][1] = 1
                    answer += 1
print(answer)
