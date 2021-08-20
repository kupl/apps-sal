A = input()
B = input()
c = 0
s = 0
i = 0
e = len(A) - len(B)
while i <= e:
    AA = A[i:i + len(B)]
    if AA == B:
        c += 1
        i += len(B) - 1
    i += 1
print(c)
