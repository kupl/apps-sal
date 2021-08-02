N, K = map(int, input().split())
num = K;

if N != 1:
    for i in range(1, N):
        num *= K - 1

print(num)
