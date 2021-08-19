(a, b) = input().split()
a = int(a)
b = int(b)
c = list(map(int, input().split()))
c.sort()
d = 0
for i in range(b):
    d = d + c[-i - 1]
print(d)
