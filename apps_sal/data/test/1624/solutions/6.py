n = int(input())
A = list(map(int, input().split()))
A.sort()
answer = 0
for i in range(n // 2):
    answer += (A[i] + A[n - i - 1]) ** 2
print(answer)
