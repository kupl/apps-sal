(n, k) = map(int, input().split())
a = 2 * n
b = 5 * n
c = 8 * n
print((a + k - 1) // k + (b + k - 1) // k + (c + k - 1) // k)
