K = int(input())
N = 50

A = K // N + 1
B = A * N - K
a = [49 + A] * N
for i in range(B):
    a[i] -= N
    for j in range(N):
        if j == i: continue
        a[j] += 1

print(N)
print(' '.join(map(str, a)))
