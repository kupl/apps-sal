(N, K) = list(map(int, input().split()))
l = list(map(int, input().split()))
l.sort()
Sum = 0
for i in range(K):
    Sum += l[N - i - 1]
print(Sum)
