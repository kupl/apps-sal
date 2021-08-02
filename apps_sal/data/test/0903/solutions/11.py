n, k = map(int, input().split())
l = list(map(int, input().split()))
l.sort()
same = 1
mid = n // 2
while k > 0:
    if same <= mid:
        diff = l[mid + same] - l[mid]
        temp = k
        k -= ((diff) * same)
        if k >= 0:
            l[mid] = l[mid + same]
        else:
            l[mid] = l[mid] + (temp // same)
    else:
        l[mid] = l[mid] + (k // (same))
        k = 0
    #print (l[mid],same)
    same += 1
print(l[mid])
