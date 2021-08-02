a, b, k = list(map(int, input().split()))
c = []
for i in range(1, min(a, b) + 1):
    if a % i == 0 and b % i == 0:
        c.append(i)
c.reverse()
print((c[k - 1]))
