n = int(input())
v = list(map(int, input().split()))
c = list(map(int, input().split()))
x = 0
for i, j in zip(v, c):
    a = i - j
    if a > 0:
        x += a
print(x)
