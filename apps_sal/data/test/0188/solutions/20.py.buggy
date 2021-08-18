import sys

n, k = map(int, input().split())
a = list(map(int, input().split()))

mid = n
side = n * 2


def removeZeroes(a):
    return [x for x in a if x > 0]


# FOR 4
for i in range(len(a)):
    if a[i] >= 4:
        while a[i] >= 4 and (mid > 0 or side > 1):
            a[i] -= 4
            if mid:
                mid -= 1
            else:
                side -= 2

# FOR 3
for i in range(len(a)):
    if not(mid > 0 or side > 1):
        break
    if a[i] == 3:
        if mid > 0:
            mid -= 1
        else:
            side -= 2
        a[i] = 0

# REMOVE GROUPS WITH 0 REMAINED
a = removeZeroes(a)

if a.count(2) + a.count(1) != len(a):
    print("NO")
    return

for i in range(len(a)):
    if a[i] == 2 and side > 0:
        side -= 1
        a[i] = 0

for i in range(len(a)):
    if a[i] == 1 and side > 0:
        side -= 1
        a[i] = 0

a = removeZeroes(a)
a.sort()
while len(a) > 0 and a[0] == 1 and a[-1] == 2 and mid > 0:
    a = a[1:-1]
    mid -= 1
if len(a) > 0 and a[0] == 1:
    if (a.count(1) + 1) // 2 <= mid:
        print("YES")
        return
    else:
        print("NO")
        return
elif len(a) > 0 and a[0] == 2:
    while len(a) > 2 and mid > 1:
        a = a[3:]
        mid -= 2
    if mid >= len(a):
        print("YES")
        return

if len(a) > 0:
    print("NO")
else:
    print("YES")
