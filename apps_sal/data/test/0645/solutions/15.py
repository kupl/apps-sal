s = input()
l = 0
for i in s:
    if i == 'a' or i == 'e' or i == 'i' or (i == 'o') or (i == 'u'):
        l += 1
    try:
        if int(i) % 2 == 1:
            l += 1
    except:
        pass
print(l)
