(n, k) = list(map(int, input().split()))
l = []
while n > 0:
    l.append(n % k)
    n //= k
print(len(l))
