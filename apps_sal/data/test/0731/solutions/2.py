(a, b, c) = list(map(int, input().split()))
ans = 0
temp = len(str(b))
while a > 0:
    cnt = '1' + '0' * temp
    d = int(cnt) - b
    cur = a // (temp * c)
    a -= min(d, cur) * c * temp
    ans += min(d, cur)
    b = int(cnt)
    temp += 1
    if cur == 0:
        break
print(ans)
