n = int(input())
s = list(input())
lets = {}
for i in s:
    try:
        lets[i] += 1
    except:
        lets[i] = 1
count = 0
centre = []
rest = []
for i in lets.keys():
    if(lets[i] % 2):
        centre.append(i)
        count += 1
    rest += [i] * (lets[i] // 2)
if(count == 0):
    t = ''
    for i in lets.keys():
        t = i * (lets[i] // 2) + t + i * (lets[i] // 2)
    print(1)
    print(t)

else:
    extra = 0
    while(n % count != 0 or (n // count) % 2 == 0):
        count += 2
        extra += 1
    for i in range(extra):
        centre += [rest.pop()] * 2
    amt = len(rest) // (count)
    temp = rest.copy()
    rest = ''
    for i in temp:
        rest += i
    print(count)
    print(rest[0:amt] + centre[0] + rest[(1) * (amt) - 1::-1], end=' ')
    for i in range(1, count):
        print(rest[i * (amt):(i + 1) * amt] + centre[i] + rest[(i + 1) * (amt) - 1:(i) * amt - 1:-1], end=' ')
    print()
