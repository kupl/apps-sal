n = int(input())
arr = list(map(int, input().split()))
mina = min(arr)
maxa = max(arr)
if maxa - mina < 2:
    print(n)
    print(*arr)
    return
a, b, c = 0, 0, 0
for i in arr:
    if i == mina:
        a += 1
    elif i == maxa:
        c += 1
    else:
        b += 1
m = max(2 * min(a, c), b // 2 * 2)
if 2 * min(a, c) > b:
    b += 2 * min(a, c)
    a, c = a - min(a, c), c - min(a, c)
else:
    a += b // 2
    c += b // 2
    b = b % 2
ans = ((str(mina) + " ") * a) + ((str(mina + 1) + " ") * b) + ((str(mina + 2) + " ") * c)
print(n - m)
print(ans[:-1])
