n = int(input())
A = [0] * 1000001
idx = 1
for i in list(map(int, input().split())):
    A[i] += 1
    if A[i] > A[idx]:
        idx = i
print(idx)
