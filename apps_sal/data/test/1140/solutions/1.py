n = int(input())
b = [int(i) for i in input().split()]
c = b.count(max(b)) * b.count(min(b))
d = max(b) - min(b)
if d == 0:
    c = n * (n - 1) // 2
print(d, c)

