ans = 0
def read_line(): return [int(i) for i in input().split()]


x0, y0 = read_line()
x1, y1 = read_line()
n = int(input())
for i in range(n):
    a, b, c = read_line()
    ans += (a * x0 + b * y0 + c) * (a * x1 + b * y1 + c) < 0
print(ans)
