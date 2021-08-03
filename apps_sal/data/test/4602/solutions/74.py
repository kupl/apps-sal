N = int(input())
K = int(input())
x = [int(c) for c in input().split()]

cnt = 0
for i in range(N):
    a = 0
    b = 0
    a = abs(x[i] - 0) * 2
    b = abs(x[i] - K) * 2
    if a <= b:
        cnt += a
    else:
        cnt += b

print(cnt)
