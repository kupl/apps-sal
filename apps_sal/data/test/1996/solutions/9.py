n = int(input())

s = set()
for i in range(ord('a'), ord('z') + 1):
    s.add(chr(i))

k = 0
fl = False
for i in range(n - 1):
    q = input().split()
    if fl:
        if q[0] == '!' or q[0] == '?':
            k += 1
    if q[0] == '.':
        for ch in q[1]:
            s.discard(ch)
    elif q[0] == '!':
        s = s.intersection(set(q[1]))
    elif q[0] == '?':
        s.discard(q[1])
    if len(s) == 1:
        fl = True
q = input()

print(k)

