(n, l) = map(int, input().split())
sum = 0
m = 1000000000.0
for i in range(n):
    sum += l + i
    if abs(m) > abs(l + i):
        m = l + i
print(sum - m)
