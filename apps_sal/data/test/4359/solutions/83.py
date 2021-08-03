a = [int(input()) for i in range(5)]

mn = a[0] % 10
for i in a:
    if i % 10 == 0:
        continue
    mn = min(mn, i % 10)

for i in a:
    if i % 10 == mn:
        mn = i
        break


ans = 0
for i in a:
    if i == mn:
        ans += i
        mn = -1
        continue
    t = ((i + 9) // 10) * 10
    ans += t

print(ans)
