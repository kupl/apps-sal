(n, price) = map(int, input().split())
history = []
ans = 0
cnt = 0
for i in range(n):
    history.append(input())
for s in history[::-1]:
    if s == 'halfplus':
        cnt = cnt * 2 + 1
    else:
        cnt *= 2
    ans += cnt / 2 * price
print(int(ans))
