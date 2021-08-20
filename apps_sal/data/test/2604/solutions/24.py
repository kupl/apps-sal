(R, d) = list(map(int, input().split()))
n = int(input())
cnt = 0
for _ in range(n):
    (x, y, r) = list(map(int, input().split()))
    s = (x ** 2 + y ** 2) ** (1 / 2)
    if s + r <= R and s - r >= R - d:
        cnt += 1
print(cnt)
