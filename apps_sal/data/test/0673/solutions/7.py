(n, k) = list(map(int, input().split()))
t = n // k
s = t * k
while s <= n:
    s += k
print(s)
