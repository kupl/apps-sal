
import copy

N = int(input())
A = list(map(int, input().split()))
s, f = list(map(int, input().split()))

B = copy.deepcopy(A)
C = A + B

l = f - s
max_list = []
max_number = 0

sumC = [0 for i in range(N)]

sumC[0] = sum(C[0:l])
for i in range(1, N):
    sumC[i] = sumC[i - 1] + C[i + l - 1] - C[i - 1]

for i in range(N):
    if sumC[i] > max_number:
        max_list = [i]
        max_number = sumC[i]
    elif sumC[i] == max_number:
        max_list.append(i)

ans_list = []
for j in max_list:
    for i in range(N):
        if j + i < N:
            if s + i <= N:
                A[j + i] = s + i
            else:
                A[j + i] = s + i - N
        else:
            if s + i <= N:
                A[j + i - N] = s + i
            else:
                A[j + i - N] = s + i - N
    ans_list.append(A[0])

print(min(ans_list))
