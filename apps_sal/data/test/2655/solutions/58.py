N = int(input())
A = list(map(int, input().split()))
A.sort(reverse=True)
circle = []
sum_val = 0
for idx in range(1, len(A)):
    sum_val += A[idx // 2]
print(sum_val)
