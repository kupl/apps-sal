N = int(input())
a = list(map(int, input().split()))
A = [0] + a + [0]

total_fee = 0
for i in range(N+1):
    total_fee += abs(A[i+1]-A[i])

ans_lst = [total_fee] * N
for j in range(N):
    ans_lst[j] -= abs(A[j+1]-A[j])
    ans_lst[j] -= abs(A[j+2]-A[j+1])
    ans_lst[j] += abs(A[j+2]-A[j])
    print(ans_lst[j])
