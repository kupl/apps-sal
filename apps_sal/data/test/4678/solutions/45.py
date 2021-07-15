N = int(input())
A = list(map(int, input().split()))
h = 0
for i in range(N-1):
    if A[i+1] >= A[i]:
        continue
    else:
        tmp = A[i] - A[i+1]
        A[i+1] += tmp
        h += tmp
print(h)

