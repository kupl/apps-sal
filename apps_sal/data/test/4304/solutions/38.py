(a, b) = map(int, input().split())
x = b - a
cnt = 0
for i in range(x + 1):
    cnt += i
print(cnt - b)
