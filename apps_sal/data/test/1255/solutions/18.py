val = 0
c = 0
prev = ''
for i in range(int(input())):
    cur = input()
    if cur == prev:
        c += 1
    else:
        c = 1
    if c > val:
        val = c
    prev = cur
print(val)
