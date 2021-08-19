(a, b) = map(int, input().split())
c = k = 0
while a:
    k += a
    (a, c) = ((a + c) // b, (a + c) % b)
print(k)
