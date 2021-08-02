n = int(input())
x = list(map(int, input().split()))

q = 0
p = 0
for i in range(n):
    for j in range(i):
        if i > j:
            if x[i] - x[j] >= 0:
                q += 1
            else:
                q = 0
                break
    if q > 0:
        p += 1
        q = 0

print((1 + p))
