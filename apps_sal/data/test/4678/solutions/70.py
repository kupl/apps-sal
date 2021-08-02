N = int(input())
A = list(map(int, input().split()))

count = 0
max_value = A[0]
for i in range(N - 1):
    # pdb.set_trace()
    if(max_value > A[i + 1]):
        count += max_value - A[i + 1]
    if (max_value < A[i + 1]):
        max_value = A[i + 1]
print(count)
