from functools import cmp_to_key as ctk
s = []
for o in range(int(input())):
    s += [input()]
s.sort(key=ctk(lambda x, y: 1 if x + y > y + x else -1))
print(''.join(s))
