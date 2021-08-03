str1 = input().split()
n = int(str1[0])
d = int(str1[1])
h = int(str1[2])

if n < h + 1:
    print(-1)
    return
elif n < d + 1:
    print(-1)
    return
elif d > h * 2:
    print(-1)
    return
elif d == h == 1 and n > 2:
    print(-1)
    return

for i in range(1, h + 1):
    print(i, i + 1)
count = n - h - 1
k = 0
left = d - h
dist = h - 1
if count > 0:
    if d - h > 0:
        count -= 1
        print(1, h + 2 + left * k)
        if count == 0:
            return
        for i in range(left - 1):
            print(i + h + 2 + left * k, i + h + 3 + left * k)
            count -= 1
            if count == 0:
                return
        k += 1
while count > 0:
    count -= 1
    if h > 1:
        print(2, n - count)
    else:
        print(1, n - count)
