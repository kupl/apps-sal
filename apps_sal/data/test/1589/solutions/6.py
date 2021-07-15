N, M = map(int, input().split())
Sum = 0
for i in range(N):
    a = list(map(int, input().split()))
    for j in range(M):
        if a[2*j] or a[2*j + 1]:
            Sum += 1
print(Sum)
