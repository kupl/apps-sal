n = int(input())
A = list(map(int, input().split()))
count = 0

for i in range(1, len(A) - 1):
    if A[i] == 0 and A[i - 1] == 1 and A[i + 1] == 1:
        A[i + 1] = 0
        count += 1

print(count)
