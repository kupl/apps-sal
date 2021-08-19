def read():
    return list(map(int, input().split()))


(n, m) = read()
a = list(read())
p = [0] * 20
for i in a:
    p[i] += 1
cnt = n * (n - 1) // 2
for i in p:
    cnt -= i * (i - 1) // 2
print(cnt)
