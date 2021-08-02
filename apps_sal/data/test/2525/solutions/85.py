import sys
S = input()
A = ''
input()
key = 1

for i in sys.stdin:
    if i[0] == '0':
        break

    if i[0] == '1':
        key = -key

    elif key == 1:
        if i[2] == '1':
            A = A + i[4]
        else:
            S = S + i[4]

    else:
        if i[2] == '2':
            A = A + i[4]
        else:
            S = S + i[4]

ans = A[::-1] + S
print((ans[::key]))
