def read(): return map(int, input().split())


R, d = read()
n = int(input())
cnt = 0
for i in range(n):
    x, y, r = read()
    p = (x ** 2 + y ** 2) ** 0.5
    if p - r >= R - d and p + r <= R:
        cnt += 1
print(cnt)
