n, k = map(int, input().split())
a = 0
while k % 2 == 0:
    a += 1
    k /= 2
print(a + 1)
