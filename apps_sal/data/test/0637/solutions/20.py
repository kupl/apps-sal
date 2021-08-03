
n = int(input())
a = input().split()
for j in range(n):
    a[j] = int(a[j])
i = 1
last = a[0]
count = 1
while (i < n and last == a[i]):
    i += 1
    count += 1
if (i < n):
    last = a[i]
    buf = 1
    i += 1
    flag = 1
    while (i < n):
        if (last == a[i]):
            buf += 1
        else:
            if (count != buf):
                flag = 0
                break
            else:
                last = a[i]
                buf = 1
        i += 1
    if ((count != buf) or (flag == 0)):
        print("NO")
    else:
        print("YES")
else:
    print("YES")
