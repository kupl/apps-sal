n = int(input())
l = [chr(i) for i in range(97, 123)]
k = 0
for i in range(n):
    (d, s) = list(map(str, input().split()))
    if d == '!' and len(l) != 1:
        h = 0
        while h < len(l):
            if not l[h] in s:
                l.pop(h)
            else:
                h += 1
    elif d == '.' and len(l) != 1:
        h = 0
        while h < len(l):
            if l[h] in s:
                l.pop(h)
            else:
                h += 1
    elif d == '?' and len(l) != 1:
        if s in l:
            l.remove(s)
    elif (d == '?' or d == '!') and i != n - 1:
        k += 1
print(k)
