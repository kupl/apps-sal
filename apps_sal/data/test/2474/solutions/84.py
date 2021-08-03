n = int(input())
c = [int(i) for i in input().split()]
f = 0
c.sort()
c.reverse()
for i in range(n):
    f = f + c[i] * (i + 2)
print(f * (4**(n - 1)) % (10**9 + 7))
