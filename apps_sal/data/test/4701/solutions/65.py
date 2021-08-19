N = int(input())
K = int(input())

# A+B=N
# A:C[i]*2
# B:C[i]+K

C = 1
for i in range(N):
    if C * 2 > C + K:
        C = C + K
    else:
        C = C * 2

print(C)
