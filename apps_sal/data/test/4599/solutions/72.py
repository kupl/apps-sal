n = int(input())
x = list(map(int, input().split()))
a = 0
b = 0
x = sorted(x)
for i in range(n):
    if i % 2 == 0:
        a += x.pop()
    else:
        b += x.pop()
print(a - b)
