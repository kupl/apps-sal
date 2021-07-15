n = int(input()); a = list(map(int, input().split()))
a.sort(); b = 0
for i in range(n): b += a[2*i]
print(b)
