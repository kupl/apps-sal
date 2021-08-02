N = int(input())
P = list(map(int, input().split()))
a = P[0]
n = 1
for i in range(N - 1):
    if a > P[i + 1]:
        a = P[i + 1]
        n += 1
print(n)
