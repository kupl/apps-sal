N = int(input())
A = list([int(x) for x in input().split()])
result = [0] * N
x = 0
for (key, i) in enumerate(A):
    if key % 2 == 0:
        x += i
    else:
        x -= i
result[0] = x
for i in range(1, N):
    result[i] = 2 * A[i - 1] - result[i - 1]
print(' '.join([str(x) for x in result]))
