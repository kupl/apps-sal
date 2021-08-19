(N, M) = map(int, input().split())
A = list(map(int, input().split()))
sum = 0
for score in A:
    sum += score
number = 0
for i in range(N):
    if A[i] >= sum / (4 * M):
        number += 1
    else:
        number += 0
print('Yes' if number >= M else 'No')
