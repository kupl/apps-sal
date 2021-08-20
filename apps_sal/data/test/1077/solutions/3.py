(n, m) = list(map(int, input().split()))
target = n // m
A = [int(i) for i in input().split()]
B = [0 for _ in range(2005)]
R = B[:]
ch = 0
for i in A:
    if i <= m:
        B[i] += 1
for i in range(2005):
    R[i] = target - B[i]
j = 1
for i in range(n):
    if A[i] > m:
        while j <= m and R[j] <= 0:
            j += 1
        if j <= m and R[j] > 0:
            ch += 1
            R[j] -= 1
            A[i] = j
for i in range(n):
    if A[i] <= m and R[A[i]] < 0:
        while j <= m and R[j] <= 0:
            j += 1
        if j <= m and R[j] > 0:
            R[j] -= 1
            R[A[i]] += 1
            A[i] = j
            ch += 1
print(target, ch)
print(*A)
