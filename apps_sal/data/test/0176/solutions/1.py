k, a, b = list(map(int, input().split()))
f = (a + k - 1) // k
l = b // k
print(l - f + 1)
