(c, r) = list(input())
c = ord(c) - ord('a')
r = ord(r) - ord('1')
if c in (0, 7) and r in (0, 7):
    print(3)
elif c in (0, 7) or r in (0, 7):
    print(5)
else:
    print(8)
