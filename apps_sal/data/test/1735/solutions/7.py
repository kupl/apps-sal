s = input()

n = 0
l = [0]
for c in s:
    if l[-1] == c:
        n += 1
        l.pop()
    else:
        l.append(c)

if n % 2 == 0:
    print("No")
else:
    print("Yes")
