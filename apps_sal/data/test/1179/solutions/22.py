def read(): return list(map(int, input().split()))


n, k = read()
a = list(read())
s = 0
for i in range(n):
    s += i + 1
    if s >= k:
        s -= i + 1
        ind = i
        break
ans = a[k - s - 1]
print(ans)
