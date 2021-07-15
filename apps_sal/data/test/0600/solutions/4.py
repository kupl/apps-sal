A, B = int(input()),int(input())

res = 0
curA = 1
curB = 1
A, B = min(A, B), max(A, B)
while A != B:
    A += 1
    res += curA
    curA += 1

    if A == B:
        break

    B -= 1
    res += curB
    curB += 1

print(res)

