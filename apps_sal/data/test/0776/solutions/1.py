(a, b, c) = list(map(int, input().split()))
m = int(input())
(USB, PS) = ([], [])
for _ in range(m):
    s = input().split()
    (l, r) = (int(s[0]), s[1])
    if r == 'USB':
        USB.append(l)
    else:
        PS.append(l)
USB.sort()
PS.sort()
a = min(a, len(USB))
res = sum(USB[:a])
USB = USB[a:]
b = min(b, len(PS))
res += sum(PS[:b])
BOTH = PS[b:] + USB
BOTH.sort()
c = min(c, len(BOTH))
res += sum(BOTH[:c])
print(str(a + b + c) + ' ' + str(res))
