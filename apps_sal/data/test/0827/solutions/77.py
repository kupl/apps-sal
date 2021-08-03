N = int(input())
T = input()

if T == '1':
    print(2 * 10**10)
    return

c = 1
if T[0] == '0':
    c1 = 0
else:
    c1 = 1

T = T[1:]

for t in T:
    if t == '1':
        if c1 == 2:
            print(0)
            return
        elif c1 == 0:
            c += 1
        c1 += 1
    if t == '0':
        if c1 == 0 or (c > 1 and c1 == 1):
            print(0)
            return
        c1 = 0

print(10**10 - c + 1)
