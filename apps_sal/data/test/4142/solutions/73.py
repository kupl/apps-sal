N = str(input())
a = ['R','U','D']
b = ['L','U','D']
c = 0
for i in range(0, len(N)):
    if i % 2 == 0:
        if N[i] in a:
            c += 1

    else:
        if N[i] in b:
            c += 1


if c == len(N):
    print('Yes')
else:
    print('No')
