(n, p) = map(int, input().split())
a = list(map(int, input().split()))
m = -1
s = sum(a)
sums = 0
for i in a:
    sums += i
    m = max(m, sums % p + (s - sums) % p)
print(m)
