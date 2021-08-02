s = input()
ls = len(s)
m = [0] * (2019)
m[0] += 1

cnt = 0
b = 0
for i in range(ls):
    a = (b + pow(10, cnt, 2019) * int(s[ls - i - 1])) % 2019
    m[a] += 1
    b = a
    cnt += 1

ans = 0
for i in m:
    if i <= 1:
        continue
    ans += i * (i - 1) // 2

print(ans)
