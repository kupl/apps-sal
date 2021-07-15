n = int(input())
s = input().split()
d = {}
for i in s:
    d[i] = d.get(i, 0) + 1
ans = 0
for i in d:
    if i == '0':
        continue
    if d[i] == 2:
        ans += 1
    elif d[i] > 2:
        print('-1')
        break
else:
    print(ans)
