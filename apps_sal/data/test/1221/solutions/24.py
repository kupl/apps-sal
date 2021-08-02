n = 0
m = 0
MaxP = 0
A = [0] * 100
B = [0] * 100
MaxV = -99999999999999999999999999999999999999

n, m = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
for i in range(n):
    for j in range(m):
        if MaxV < A[i] * B[j]:
            MaxP = i
            MaxV = A[i] * B[j]

MaxV = -99999999999999999999999999999999999999999
for i in range(n):
    if i != MaxP:
        for j in range(m):
            if MaxV < A[i] * B[j]:
                MaxV = A[i] * B[j]

print(MaxV)
