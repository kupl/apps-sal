n, m, k = list(map(int, input().split()))
A = list(map(int, input().split()))

m -= 1


min_dist = n + 1
min_index = -1
for i in range(len(A)):
    if A[i] != 0 and A[i] <= k and abs(i - m) <= min_dist:
        min_index = i
        min_dist = abs(i - m)


print(min_dist * 10)
