n = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
a_sum = 0
b_sum = 0
for i in range(n):
    a_sum |= A[i]
    b_sum |= B[i]
print(a_sum + b_sum)
