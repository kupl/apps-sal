n = int(input())
s = input()
a = []
cur = 0
for i in s:
    if i == 'B':
        cur += 1
    elif cur:
        a.append(cur)
        cur = 0
if cur:
    a.append(cur)
print(len(a))
print(*a)
