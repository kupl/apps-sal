n = int(input())
x = []
y = []
m = 101
r = 0
for i in range(n):
    a, b = list(map(int, input().split()))
    if b < m:
        m = b
    r = r + a * m

print(r)
