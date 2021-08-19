(n, m) = map(int, input().split())
c = [0] * n
s = list(map(int, input().split()))
for sq in s:
    c[sq - 1] += 1
print(min(c))
