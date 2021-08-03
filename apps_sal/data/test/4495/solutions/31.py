a, b, x = list(map(int, input().split()))
res = b // x - (a + x - 1) // x + 1
print(res)
