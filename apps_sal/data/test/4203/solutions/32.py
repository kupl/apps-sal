A = input()
B = A.lower()
C = 0
for i in range(len(A)):
    if A[i] != B[i]:
        C += 1
if A[0] != 'A' or C != 2:
    print('WA')
elif 'C' in A[2:-1]:
    print('AC')
else:
    print('WA')
