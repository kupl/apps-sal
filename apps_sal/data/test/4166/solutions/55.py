n, m = map(int, input().split())
data = [-1] * n
for i in range(m):
    s, c = map(int, input().split())
    if (s == 1 and c == 0) and n >= 2:
        print(-1)
        return
    if data[s - 1] == -1 or data[s - 1] == c:
        data[s - 1] = c
    elif data[s - 1] != -1 and data[s - 1] != c:
        print(-1)
        return

if data[0] == -1 and n != 1:
    data[0] = 1
elif data[0] == -1 and n == 1:
    data[0] = 0
for i in range(1, n):
    if data[i] == -1:
        data[i] = 0
print(*data, sep='')
