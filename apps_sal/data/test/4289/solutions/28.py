N = int(input())
T, A = list(map(int, input().split()))
X = list(map(int, input().split()))

s = 10000

for i in range(N):
    x = T - X[i] * 0.006
    if abs(A - x) < s:
        ans = i
        s = abs(A - x)
print((ans + 1))
