n = int(input())
d, x = map(int, input().split())

for i in range(n):
    a = int(input())
    b = 1
    while b <= d:
        x += 1
        b += a
print(x)
