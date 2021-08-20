def isSorted(l):
    i = 1
    while i < len(l):
        if l[i] < l[i - 1]:
            return False
        i += 1
    return True


n = int(input())
a = list(map(int, input().split()))
s = e = 0
i = 1
b = list()
while i < len(a):
    if a[i] > a[i - 1]:
        i += 1
    else:
        s = i - 1
        while i < n and a[i] < a[i - 1]:
            i += 1
        e = i - 1
        b = a[0:s] + list(reversed(a[s:e + 1])) + a[e + 1:]
        break
if isSorted(b):
    print('yes')
    print(s + 1, e + 1, sep=' ')
else:
    print('no')
