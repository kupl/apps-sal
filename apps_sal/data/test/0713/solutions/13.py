n, m = list(map(int, input().split()))

a = min(n, m)
print(a + 1)
for i in range(a + 1):
    print(i, a - i)
