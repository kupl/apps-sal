(N, M) = map(int, input().split())
A = set([int(input()) for _ in range(M)])
step = [0] * (N + 1)
step[0] = 1
if 1 not in A:
    step[1] = 1
else:
    step[1] = 0
for i in range(2, N + 1):
    if i in A:
        continue
    step[i] = (step[i - 1] + step[i - 2]) % 1000000007
print(step[-1])
