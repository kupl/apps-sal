N = int(input())
A = [int(input()) for i in range(N)]
sorted_A = sorted(A, reverse=True)
(max_value, next_value) = (sorted_A[0], sorted_A[1])
for i in A:
    if i == max_value:
        print(next_value)
    else:
        print(max_value)
