from functools import cmp_to_key
a = []
n = int(input())
for i in range(n):
    a.append(input())
a.sort(key=cmp_to_key(lambda x, y: 1 if x + y > y + x else -1))
print(''.join(a))
