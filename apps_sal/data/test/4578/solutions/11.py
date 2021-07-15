N, X = map(int, input().split())
a = list(int(input()) for _ in range(N))
count = 0

for i in range(N):
    X = X - a[i]
if X / min(a) >= 1:
    count += X // min(a)
print(N+count)
