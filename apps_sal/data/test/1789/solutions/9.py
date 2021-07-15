a, b, x, y = map(int, input().split())

dif = a-b
elv = min(2*x, y)

if dif > 0:
    ans = (dif-1)*elv + x
else:
    ans = -dif*elv + x

print(ans)
