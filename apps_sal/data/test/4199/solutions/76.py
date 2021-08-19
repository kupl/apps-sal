(N, K) = map(int, input().split())
h = list(map(int, input().split()))
a = 0
for i in h:
    if i >= K:
        a += 1
print(a)
