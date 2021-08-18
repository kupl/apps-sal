N = int(input())
A = list(map(int, input().split()))
A = sorted(A)
if N == 2:
    print(sum(A) / 2)
    return
else:
    temp = (A[0] + A[1]) / 2
    for i in range(2, N):
        temp = 1 / 2 * (A[i] + temp)
print(temp)
