N = int(input())
K = int(input())
v = 1
for _ in range(N):
    if v <= K:
        v *= 2
    else:
        v += K
print(v)
