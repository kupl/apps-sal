import sys
S = input()
Q = int(input())
key = 1
for i in sys.stdin:
    if i[0] == '0':
        break
    if i[0] == '1':
        key = -key
    elif key == 1:
        if i[2] == '1':
            S = i[4] + S
        else:
            S = S + i[4]
    elif i[2] == '2':
        S = i[4] + S
    else:
        S = S + i[4]
print(S[::key])
