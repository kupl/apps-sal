a = [int(input())]

i = 0
while True:
    if a[i]%2 == 0:
        a.append(int(a[i]/2))
    else:
        a.append(int((3*a[i])+1))
    if a.count(a[i]) == 2:
        break
    i += 1

print(i+1)
