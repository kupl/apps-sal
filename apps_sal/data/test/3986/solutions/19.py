li = list(map(int, input().split()))
n = li[0]
k = li[1]
s = ''
if k > n or (k < 2 and n != 1) or k == 0:
    print(-1)
else:
    if n - k == 0:
        for i in range(97, 97 + k):
            s += chr(i)
    else:
        for i in range(n - (k - 2)):
            if i % 2 == 0:
                s += chr(97)
            else:
                s += chr(98)
    if n != k:
        for i in range(99, 99 + (k - 2)):
            s += chr(i)
print(s)
