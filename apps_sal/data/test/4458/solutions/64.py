N = int(input())
P = list(map(int, input().split()))
a = 0
for p in P:
    if p <= N:
        a += 1
        N = p
print(a)
