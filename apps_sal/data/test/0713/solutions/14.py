(n, m) = list(map(int, input().split()))
lo = min([n, m]) + 1
print(lo)
for i in range(lo):
    print(i, lo - i - 1)
