N = int(input())
K = int(input())
s = 1
for _ in range(N):
    s = min(s * 2, s + K)
print(s)
