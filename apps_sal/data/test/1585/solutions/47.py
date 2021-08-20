(x, y) = map(int, input().split())
(x, y) = (1, y // x)
cnt = 0
while x <= y:
    x *= 2
    cnt += 1
print(cnt)
