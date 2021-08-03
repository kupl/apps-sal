n, x, y = map(int, input().split())
s = input()
cnt = 0
for i in range(n - x, n):
    if s[i] == '1':
        if i != n - y - 1:
            cnt += 1
    elif i == n - y - 1:
        cnt += 1
print(cnt)
