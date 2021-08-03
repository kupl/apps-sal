n = int(input())
a = list(map(int, input().split()))
d = 0
m = 10**9 + 7
for i in range(60):
    b = 1 << i
    l = len([1for j in a if j & b])
    d += l * (n - l) * b % m
    d %= m
print(d)
