n = int(input())
a = list(map(int, input().split()))
count = 0
r = 1
l = 0
now = a[0]
while l < n:

    while True:
        if r < n and now + a[r] == now ^ a[r]:
            now += a[r]
            count += r - l
            r += 1
        else:
            break
    if l == r:
        now = a[l]
        r += 1
    elif l < n:
        now -= a[l]
        l += 1
print(count + n)
