l = input().split(" ")
l2 = [int(i) for i in l]
A = min(l2)
l2.remove(A)
C = max(l2)
l2.remove(C)
B = l2[0]


count = 0
if A == B == C:
    pass
else:
    n = C - B
    if n % 2 == 0:
        count = count + (n // 2)
        B = C
    else:
        count = count + (n // 2) + 1
        B = C
        A = A + 1
    m = C - A
    if m % 2 == 0:
        count = count + (m // 2)
    else:
        count = count + (m // 2) + 2
        

print(count)

