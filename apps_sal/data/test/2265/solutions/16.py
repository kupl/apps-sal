
A = input()

B = input()

B_zeros = 0

for i in range(len(B)):
    if B[i] == '0':
        B_zeros += 1


L_B = len(B)
zeros = 0
res = 0
for i in range(len(A)):
    if A[i] == '0':
        zeros += 1

    if i == L_B - 1:
        do = 1
    elif i > L_B - 1:
        if A[i - L_B] == '0':
            zeros -= 1

    if i >= L_B - 1:
        if (zeros - B_zeros) % 2 == 0:
            res += 1

print(res)
