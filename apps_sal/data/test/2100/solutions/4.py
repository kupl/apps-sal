n = int(input())
a = b = 0
for i in range(n):
    x, y = list(map(int, input().split()))
    a += x;
    b += y;
print(min(a, n - a) + min(b, n - b))
