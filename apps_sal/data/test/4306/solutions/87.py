lst = input().split()

A = int(lst[0])
B = int(lst[1])
C = int(lst[2])
D = int(lst[3])

if (B <= C) or (D <= A):
    print(0)
elif (A <= C <= B) and (C <= B <= D):
    print(B - C)
elif (C <= A <= D) and (A <= D <= B):
    print(D - A)
else:
    print(min([B - A, D - C]))
