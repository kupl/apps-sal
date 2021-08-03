n, m = (int(i) for i in input().split())
A = [int(i) for i in input().split()]
B = [int(i) for i in input().split()]
tmp_a, tmp_b = A[0], B[0]
nbf = 0
i = j = 0
while i < n or j < m:
    while tmp_a > tmp_b and j < m:
        #~ print("tmp_b",tmp_b,"< tmp_a",tmp_a,"i",i,"j",j)
        j += 1
        tmp_b += B[j]
    while tmp_b > tmp_a and i < n:
        #~ print("tmp_b",tmp_b,"> tmp_a",tmp_a,"i",i,"j",j)
        i += 1
        tmp_a += A[i]
    if tmp_a == tmp_b:
        #~ print("tmp_b",tmp_b,"= tmp_a",tmp_a,"i",i,"j",j,"nb_f",nbf)
        nbf += 1
        i += 1
        j += 1
        if i < n:
            tmp_a = A[i]
        if j < m:
            tmp_b = B[j]
print(nbf)
