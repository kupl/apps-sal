n, k = map(int, input().split())

for x in range(k):
    if n%10:
        n -= 1
    else:
        n //= 10

print(n)
