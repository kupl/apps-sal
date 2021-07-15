N = int(input())
d = list(map(int, input().split()))

s = 0
for i in range(N):
    for j in range(i+1, N):
        s += d[i] * d[j]

print(s)
