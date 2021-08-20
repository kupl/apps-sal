s = input().strip()
c = 0
for z in s:
    if z in 'aeiou':
        c += 1
    else:
        try:
            u = int(z)
            if u % 2 == 1:
                c += 1
        except:
            pass
print(c)
