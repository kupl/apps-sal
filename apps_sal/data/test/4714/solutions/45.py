a, b = list(map(int, input().split()))
cnt = 0

for i in range(b - a + 1):
    r = str(a + i)[::-1]
    if a + i == int(r):
        cnt += 1
print(cnt)
