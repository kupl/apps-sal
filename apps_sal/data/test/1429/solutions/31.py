(N, S) = input().split()
N = int(N)
count = 0
for i in range(N):
    num_A = num_T = num_C = num_G = 0
    for char in S[i:N]:
        if char == 'A':
            num_A += 1
        elif char == 'T':
            num_T += 1
        elif char == 'C':
            num_C += 1
        else:
            num_G += 1
        if num_A == num_T and num_C == num_G:
            count += 1
print(count)
