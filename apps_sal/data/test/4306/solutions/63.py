l = list(map(int, input().split()))
if l[1] < l[2]:
    print(0)
elif l[0] > l[3]:
    print(0)
else:
    l.sort()
    print(l[2] - l[1])
