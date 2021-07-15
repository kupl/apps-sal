import math

L = int(input())

A = input()
len_A = len(A)

if len_A % L != 0:
    print(('1'+'0'*(L-1))*math.ceil(len_A/L))
else:
    p = A[:L]
    intp = p*int(len_A/L)

    if intp > A:
        print(intp)
    elif p.count('9') == L:
        print(('1'+'0'*(L-1))*(int(len_A/L)+1))
    else:
        print(str(int(p)+1)*int(len_A/L))

