a = list(map(int, input()))
b = list(map(int, input()))

ps = [0] * (len(b) + 1)
for i in range(len(b)):
    ps[i + 1] = ps[i] + b[i]

ans = 0
for i in range(len(a)):
    left = i
    right = len(b) - len(a) + i + 1
    sub = ps[right] - ps[left]
    if a[i] == 1:
        sub = right - left - sub
    ans += sub
print(ans)
