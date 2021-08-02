from functools import cmp_to_key


def f(x, y):
    return -1 if x + y < y + x else 1


n = int(input())
A = []
for i in range(n):
    s = input()
    A.append(s)
print(''.join(sorted(A, key=cmp_to_key(f))))
