import math
n = int(input())
arr = list(map(int, input().split()))
tb = {}

for i in range(n):
    if arr[i] in tb:
        x = arr[i]
        while x in tb:
            y = tb.pop(x)
            if 2 * x not in tb:
                tb[2 * x] = i
                break
            x = 2 * x
    else:
        tb[arr[i]] = i

s = ''
print(len(tb))
key = list(tb.keys())
ans = []
for i in key:
    ans.append([tb[i], i])

ans.sort()

for i in ans:
    s += str(i[1]) + " "


print(s)
