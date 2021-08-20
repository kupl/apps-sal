N = int(input())
A = [int(a) for a in input().split()]
X = [0] * 20
for a in A:
    for i in range(20):
        if a >> i & 1:
            X[i] += 1
m = (1 << 20) - 1
s = m
ans = 0
for i in range(N):
    for j in range(20):
        if X[j] == i:
            s ^= 1 << j
    ans += s * s
print(ans)
