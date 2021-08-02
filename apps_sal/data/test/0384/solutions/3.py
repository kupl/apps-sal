n = int(input())
s = input()
cur = 0
a = []
for elem in s:
    if elem == 'B':
        cur += 1
    else:
        if cur != 0:
            a.append(cur)
            cur = 0
if cur != 0:
    a.append(cur)
print(len(a))
print(' '.join(map(str, a)))
