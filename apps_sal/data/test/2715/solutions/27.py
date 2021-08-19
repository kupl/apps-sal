K = int(input())
N = 50
Q = K // N
R = K % N
print(N)
for i in range(R):
    print(N - 1 + Q - R + N + 1, end=' ')
for i in range(N - R):
    print(N - 1 + Q - R, end=' ')
