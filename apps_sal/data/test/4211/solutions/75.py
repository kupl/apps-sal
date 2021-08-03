N = int(input())
B = list(map(int, input().split()))
print((B[0] + B[-1] + sum(min(B[i], B[i + 1]) for i in range(N - 2))))
