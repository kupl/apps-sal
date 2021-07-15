a, b = map(int, input().split())

c = b - a

height_a = 0
for i in range(1, c):
    height_a += i
ans = height_a - a

print(ans)
