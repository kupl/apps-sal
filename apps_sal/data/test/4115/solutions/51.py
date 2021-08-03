import math
A = input()
times = math.ceil(len(A) / 2)
count = 0
for i in range(times):
    if A[i] != A[len(A) - 1 - i]:
        count += 1
print(count)
