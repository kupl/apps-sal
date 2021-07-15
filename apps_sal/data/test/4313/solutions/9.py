N = int(input())
V = list(map(int, input().split()))
C = list(map(int, input().split()))

total = 0
for i, j in zip(V, C):
    s = i - j
    if s > 0:
        total += s
print(total)
