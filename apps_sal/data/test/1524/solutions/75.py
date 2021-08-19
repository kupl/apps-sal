S = input()
A = [0] * len(S)
n = 0
m = 0
num = 0
for i in range(len(S)):
    if S[i] == 'R':
        if num % 2 == 0:
            n += 1
        else:
            m += 1
        num += 1
    else:
        if num > 0:
            if num % 2 == 0:
                A[i] += n
                A[i - 1] += m
            else:
                A[i] += m
                A[i - 1] += n
        n = 0
        m = 0
        num = 0
sle = S[::-1]
n = 0
m = 0
num = 0
for i in range(len(S)):
    if sle[i] == 'L':
        if num % 2 == 0:
            n += 1
        else:
            m += 1
        num += 1
    else:
        if num % 2 == 0:
            A[-(i + 1)] += n
            A[-i] += m
        else:
            A[-(i + 1)] += m
            A[-i] += n
        n = 0
        m = 0
        num = 0
for i in A:
    print(i, end=' ')
