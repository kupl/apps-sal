N = int(input())
A = list(map(int, input().split()))
res = [-1] * N

for i in reversed(range(1, N + 1)):
    p = (N // i) * i
    s = 0
    while res[p - 1] != -1:
        s += res[p - 1]
        s %= 2
        p -= i
    res[p - 1] = (A[p - 1] - s) % 2

print(sum(res))
for i in range(N):
    if res[i] == 1:
        print(i + 1)
