(n, k) = input().split()
k = int(k)
l = len(n)
s = list(reversed(list(map(int, n))))
c = 0
n = 0
while c < k:
    try:
        if s[c] == 0:
            c += 1
        else:
            s.pop(c)
            n += 1
    except IndexError:
        break
if s[-1] == 0:
    print(l - 1)
else:
    print(n)
