a, b = map(int, input().split())
c = b - a
cnt = 0
for i in range(c):
    cnt += (i + 1)
print(cnt - b)
