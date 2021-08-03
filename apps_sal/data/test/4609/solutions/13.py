n = int(input())
kami = set()

for i in range(n):
    a = int(input())
    if a in kami:
        kami.remove(a)
    else:
        kami.add(a)

print((len(kami)))
