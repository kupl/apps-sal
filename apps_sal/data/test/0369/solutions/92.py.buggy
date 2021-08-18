n, m = map(int, input().split())
s = list(str(input()))
s = list(reversed(s))
# print(s)

ds = []
d = 1
for i in range(1, n + 1):
    if s[i] == '0':
        ds.append(d)
        d = 1
    else:
        d += 1
# print(ds)

temp0 = 0
ans = []
for i in range(len(ds)):
    if ds[i] > m:
        print(-1)
        return
    temp1 = temp0 + ds[i]
    # print(temp1)
    if temp1 > m:
        ans.append(temp0)
        temp0 = ds[i]
    elif temp1 == m:
        ans.append(temp1)
        temp0 = 0
    else:
        temp0 = temp1
else:
    if temp0 != 0:
        ans.append(temp0)
ans = list(reversed(ans))
print(*ans)
