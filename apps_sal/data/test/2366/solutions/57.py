N = int(input())
A = input().split()
num_list = [0] * N


def combination(n):
    C = [0]
    for i in range(2, n + 1):
        C.append(int(i * (i - 1) / 2))
    return C


com = combination(N)
sum_com = 0
for i in range(N):
    num_list[int(A[i]) - 1] += 1
for i in range(N):
    if num_list[i] == 0:
        continue
    else:
        sum_com += com[num_list[i] - 1]
for i in range(N):
    print(sum_com - num_list[int(A[i]) - 1] + 1)
