
a = list(input())
i = 0
k = 0
l = len(a)
while i < l:
    if a[i] <= chr(97 + k):
        if k < 26:
            a[i] = chr(97 + k)
            k += 1
    i += 1
if k == 26:
    print(''.join(a))
else:
    print(-1)
