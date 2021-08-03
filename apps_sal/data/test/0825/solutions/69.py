a, n = 0, int(input())
for i in range(2, int(n**0.5 + 1)):
    x = 0
    while(n % i == 0):
        n //= i
        x += 1
    j = 1
    while(x >= j):
        a += 1
        x -= j
        j += 1
print(a + (n > 1))
