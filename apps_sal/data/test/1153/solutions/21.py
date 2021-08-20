(n, m) = (int(i) for i in input().split())
A = [int(i) for i in input().split()]
B = [int(i) for i in input().split()]
(tmp_a, tmp_b) = (A[0], B[0])
nbf = 0
i = j = 0
while i < n or j < m:
    while tmp_a > tmp_b and j < m:
        j += 1
        tmp_b += B[j]
    while tmp_b > tmp_a and i < n:
        i += 1
        tmp_a += A[i]
    if tmp_a == tmp_b:
        nbf += 1
        i += 1
        j += 1
        if i < n:
            tmp_a = A[i]
        if j < m:
            tmp_b = B[j]
print(nbf)
