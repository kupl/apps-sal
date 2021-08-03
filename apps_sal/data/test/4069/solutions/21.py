a = input().split(" ")
b = [x, k, d] = [int(a[0]), int(a[1]), int(a[2])]
ans = 0
if x - k * d > 0:
    ans = x - k * d
elif x + k * d < 0:
    ans = - k * d - x
else:
    if k % 2 == 0:
        ans = x % (2 * d)
        if d < x % (2 * d):
            ans = 2 * d - x % (2 * d)
    elif k % 2 == 1:
        ans = (x + d) % (2 * d)
        if d < (x + d) % (2 * d):
            ans = 2 * d - (x + d) % (2 * d)
print(ans)
