__author__ = 'Snopi'

s = input()
k = int(input())
if len(s) % k != 0:
    print("NO")
    return

o = len(s) // k

for j in range(k):
    lal = s[j*o:(j + 1)*o]
    if lal != "".join(reversed(lal)):
        print("NO")
        return

print("YES")
