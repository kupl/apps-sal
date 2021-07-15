n = int(input())
A = []
for i in range(n):
    A.append(input())
def custom_sort(s1,s2):
    if (s1+s2) <= (s2+s1):
        return -1
    else:
        return 1

import functools
A.sort(key=functools.cmp_to_key(custom_sort))
print("".join(A))
