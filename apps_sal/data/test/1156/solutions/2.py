n = int(input())
a = [int(x) for x in input().split(' ')]
b = input()

llow = -1000000000
lhigh = 1000000000
rlow = -1000000000
rhigh = 1000000000

i = 4
last = 0
while i < n:
    if int(b[i]) == last:
        if last == 1:
            if min(a[i - 4:i + 1]) > rlow:
                rlow = min(a[i - 4:i + 1])
        else:
            if max(a[i - 4:i + 1]) < llow:
                lhigh = max(a[i - 4:i + 1])

        i += 1
    else:
        if last == 1:
            if min(a[i - 4:i + 1]) <= rhigh:
                rhigh = min(a[i - 4:i + 1]) - 1
        else:
            if max(a[i - 4:i + 1]) >= llow:
                llow = max(a[i - 4:i + 1]) + 1

        last = 1 - last
        i += 4

    if llow == lhigh and rlow == rhigh:
        break

print(str(llow) + ' ' + str(rhigh))
