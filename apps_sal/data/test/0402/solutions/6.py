def read(): return list(map(int, input().split()))


n, k = read()
t = 240 - k
cur = 0
for i in range(1, n + 1):
    c = 5 * i
    if cur + c > t:
        ans = i - 1
        break
    cur += c
else:
    ans = n
print(ans)
