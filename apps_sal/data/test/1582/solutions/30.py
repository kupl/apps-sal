n = int(input())
hist = [[0 for _ in range(10)] for _ in range(10)]
ans = 0
for i in range(1, n + 1):
    top = int(str(i)[0])
    bot = int(str(i)[-1])
    hist[top][bot] += 1
for i in range(1, n + 1):
    top = int(str(i)[0])
    bot = int(str(i)[-1])
    ans += hist[bot][top]
print(ans)
