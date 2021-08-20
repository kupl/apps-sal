(K, N) = map(int, input().split())
A = [int(a) for a in input().split()]
A.append(A[0] + K)
b = []
max = 0
sum = 0
for i in range(N):
    t = A[i + 1] - A[i]
    sum += t
    if max < t:
        max = t
sum -= max
print(sum)
