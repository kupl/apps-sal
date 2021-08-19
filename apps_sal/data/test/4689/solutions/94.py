(K, N) = list(map(int, input().split()))
A = [int(x) for x in input().split()]
mx = A[0] + K - A[-1]
for i in range(len(A) - 1):
    dis = A[i + 1] - A[i]
    if dis > mx:
        mx = dis
print(K - mx)
