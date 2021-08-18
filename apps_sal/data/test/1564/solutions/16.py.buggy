n = int(input())
s = input()
t = input()

ab = []
ba = []

for i in range(n):
    if (s[i] != t[i]):
        if (s[i] == 'a'):
            ab.append(i)
        else:
            ba.append(i)

if ((len(ab) + len(ba)) % 2 > 0):
    print(-1)
    return

swaps = []

while (len(ab) > 1):
    swaps.append((ab.pop(), ab.pop()))

while (len(ba) > 1):
    swaps.append((ba.pop(), ba.pop()))

if (len(ab) > 0):
    t1 = ab.pop()
    t2 = ba.pop()
    swaps.append((t1, t1))
    swaps.append((t1, t2))

print(len(swaps))
for (t1, t2) in swaps:
    print(t1 + 1, t2 + 1)
