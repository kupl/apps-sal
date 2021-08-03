n, m = [int(x) for x in input().split()]
r = 0
for i in range(5):
    r += ((n + (5 - i) % 5) // 5) * ((m + i) // 5)
print(r)
