s = input()
x = s[0]
y = int(s[1])
l = 0
if x == 'a' or x == 'h':
    l += 1
if y == 1 or y == 8:
    l += 1
if l == 0:
    print(8)
elif l == 1:
    print(5)
else:
    print(3)
