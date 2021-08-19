s = input()
l = len(s)
k = [0 for i in range(l)]
start = 0
while True:
    temp = s.find('heavy', start, l)
    if temp == -1:
        break
    else:
        k[temp] = 1
        start = temp + 1
start = 0
while True:
    temp = s.find('metal', start, l)
    if temp == -1:
        break
    else:
        k[temp] = 2
        start = temp + 1
sol = 0
ones = 0
for i in range(l):
    if k[i] == 1:
        ones += 1
    elif k[i] == 2:
        sol += ones
print(sol)
