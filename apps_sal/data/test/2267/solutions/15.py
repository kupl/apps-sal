from functools import cmp_to_key
n = int(input())
S = []
for i in range(n):
    S.append(input())
S.sort(key=cmp_to_key(lambda x, y: 1 if x + y > y + x else -1))
print(''.join(S))
