import functools
n = int(input())
A = []
for i in range(n):
    A.append(input())


def custom_sort(s1, s2):
    n1 = len(s1)
    n2 = len(s2)
    if n1 == n2:
        if s1 <= s2:
            return -1
        else:
            return 1
    elif s1 + s2 <= s2 + s1:
        return -1
    else:
        return 1


A.sort(key=functools.cmp_to_key(custom_sort))
print(''.join(A))
