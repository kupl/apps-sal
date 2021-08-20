def r():
    return int(input())


n = r()
m = r()
a = sorted([r() for i in range(n)], reverse=1)
cnt = cur = i = 0
while cur < m:
    cur += a[i]
    cnt += 1
    i += 1
print(cnt)
