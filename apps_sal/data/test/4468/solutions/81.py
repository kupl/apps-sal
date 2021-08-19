(N, T) = map(int, input().split())
t = list(map(int, input().split()))
Sum = T
for i in range(1, N):
    if t[i] - t[i - 1] < T:
        Sum += t[i] - t[i - 1]
    else:
        Sum += T
print(Sum)
