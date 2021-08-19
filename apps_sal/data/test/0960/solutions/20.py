(n, k) = map(int, input().split())
q = 0
w = k
while q == 0:
    w -= 1
    if n % w == 0:
        q = n // w
print(q * k + w)
