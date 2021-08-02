n, h, k = list(map(int, input().split()))
a = list(map(int, input().split()))
num = 0
time = 0
s = 0
while num < n:
    time += 1
    while num < n and a[num] + s <= h:
        s += a[num]
        num += 1
    s = max(s - k, 0)
    if num < n and s > h - a[num]:
        d = (s - h + a[num] + k - 1) // k
        time += d
        s = max(s - d * k, 0)
print(time + (s + k - 1) // k)
