n, l = map(int, input().split())

T = [l + i for i in range(n)]

if T[-1] >= 0:
    m = min((i for i in T if i >= 0))
else:
    m = T[-1]

print(sum(T) - m)
