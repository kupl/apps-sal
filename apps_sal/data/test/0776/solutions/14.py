(a, b, c) = list(map(int, input().split()))
m = int(input())
z = 0
A = []
B = []
su = 0
for i in range(m):
    s = input().split()
    if s[1] == 'USB':
        A.append(int(s[0]))
    else:
        B.append(int(s[0]))
A.sort()
B.sort()
if a < len(A):
    su += sum(A[:a])
    A = A[a:]
    z += a
    a = 0
else:
    su += sum(A)
    z += len(A)
    a += -len(A)
    A = []
if b < len(B):
    su += sum(B[:b])
    B = B[b:]
    z += b
    b = 0
else:
    su += sum(B)
    z += len(B)
    b += -len(B)
    B = []
i = 0
j = 0
while c > 0 and len(A) > i and (len(B) > j):
    if A[i] == B[j]:
        if len(A) - 1 - i > len(B) - 1 - j:
            su += A[i]
            i += 1
        else:
            su += B[j]
            j += 1
    elif min(A[i], B[j]) == A[i]:
        su += A[i]
        i += 1
    else:
        su += B[j]
        j += 1
    c += -1
    z += 1
su += sum(B[j:j + c]) + sum(A[i:i + c])
z += len(B[j:j + c]) + len(A[i:i + c])
print(z, su)
