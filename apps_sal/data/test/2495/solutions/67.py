n = int(input())
a = list(map(int, input().split()))
ans = 0
b = 0
for i in range(0, n):
    if i % 2 == 1:
        if b + a[i] < 1:
            ans += abs(b + a[i]) + 1
            b = 1
        else:
            b += a[i]
    elif b + a[i] > -1:
        ans += abs(b + a[i]) + 1
        b = -1
    else:
        b += a[i]
ansa = 0
bb = 0
for i in range(n):
    if i % 2 == 0:
        if bb + a[i] < 1:
            ansa += abs(bb + a[i]) + 1
            bb = 1
        else:
            bb += a[i]
    elif bb + a[i] > -1:
        ansa += abs(bb + a[i]) + 1
        bb = -1
    else:
        bb += a[i]
print(min(ans, ansa))
