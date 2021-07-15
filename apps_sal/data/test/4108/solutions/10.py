import collections

A = input()
B = input()

A_c = collections.Counter(A)
B_c = collections.Counter(B)
A_c = list(A_c.values())
B_c = list(B_c.values())

A_c = list(A_c)
B_c = list(B_c)
A_c.sort()
B_c.sort()
if A_c == B_c:
    print("Yes")
else:
    print("No")

