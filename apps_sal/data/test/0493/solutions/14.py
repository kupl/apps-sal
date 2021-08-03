n = int(input())
s = input()
c = k = l = r = 0
for i in range(n):
    if s[i] == '.':
        if k == 0:
            c += 1
    else:
        if s[i] == 'L':
            k -= 1
            l = i
        else:
            k += 1
            r = i
        if k < 0:
            k = 0
            c = 0
        elif k == 0:
            c += (l - r + 1) % 2
print(c)
