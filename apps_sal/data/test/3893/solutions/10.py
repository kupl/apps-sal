
x, y = list(map(int, input().split()))
u, v = list(map(int, input().split()))
n = int(input())
s = 0
for i in range(n):
    a, b, c = list(map(int, input().split()))
    s += (a * x + b * y + c > 0) ^ (a * u + b * v + c > 0)
print(s)
