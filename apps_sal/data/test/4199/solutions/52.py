(N, K) = map(int, input().split())
h = list(map(int, input().split()))
x = 0
for i in h:
    if i >= K:
        x += 1
print(x)
