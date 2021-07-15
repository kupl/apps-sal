n = int(input())
a = [int(x) for x in input().split()]
c = 0
for i in a:
    c += (i % 2)
print(min(c, n - c))
